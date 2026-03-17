import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import pygetwindow as gw
import time
import ctypes
from pynput import keyboard
import win32api
import win32event
import winerror
import os
import sys 
from winotify import Notification
from collections import deque

def resource_path (relative_path):
    try :
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

mutex = win32event.CreateMutex(None, False, "WPM_Tracker_Unique_Mutex_Name")

def check_singleton():
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        sys.exit(0)


class WordFinalOverlay:

    def __init__(self):
        self.show_startup_notification()

        self.char_count = 0
        self.keypress_times = deque()
        self.start_time = None
        self.last_type_time = 0
        self.wpm = 0
        self.is_transparent = False
        
        # Dimensi Widget
        self.widget_w = 260 
        self.widget_h = 90 # Ditambah sedikit agar tidak sesak

        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg='white', highlightbackground="black", highlightthickness=2)

        # Load GIF
        self.gif_data = {
            'typing': self.load_gif("typing.gif"), 
            'wait': self.load_gif("wait.gif")}
        self.current_gif = 'wait'
        self.frame_idx = 0

        # --- Tombol Close (x) ---
        # Menggunakan fg black agar kontras
        self.close_btn = tk.Label(self.root, text="x", font=("Arial", 11), bg="white", fg="black", cursor="hand2")
        self.close_btn.place(x=self.widget_w - 25, y=5)
        # Bind manual untuk memastikan klik terdeteksi
        self.close_btn.bind("<Button-1>", lambda e: self.root.destroy())

        # --- Center Content ---
        self.center_frame = tk.Frame(self.root, bg='white')
        self.center_frame.place(relx=0.5, rely=0.45, anchor='center')

        self.img_label = tk.Label(self.center_frame, bg='white')
        self.img_label.pack(side='left', padx=10)

        self.wpm_label = tk.Label(self.center_frame, text="WPM : 00", fg="black", bg="white", font=("Segoe UI", 18, "bold"))
        self.wpm_label.pack(side='left', padx=5)

        # --- Tombol Reset ---
        # Posisi Y dinaikkan sedikit agar tidak terpotong border (y=self.widget_h - 30)
        self.reset_btn = tk.Label(self.root, text="reset", font=("Segoe UI", 10, "underline"), bg="white", fg="black", cursor="hand2")
        self.reset_btn.place(x=self.widget_w - 60, y=self.widget_h - 30)
        self.reset_btn.bind("<Button-1>", lambda e: self.reset_counter())

        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
        self.animate_loop() 
        self.sync_loop()   
        self.root.mainloop()

    def show_startup_notification(self):
        try:
            toast = Notification(
                app_id="WPM Tracker",
                title="WPM Tracker",
                msg="WPM Started..."
            )

            toast.show()

        except Exception as e: 
            print("Notification error", e)

    def load_gif(self, filename):
        frames = []
        path = resource_path(filename)

        if not os.path.exists(path): return []
        try:
            img = Image.open(path)
            for frame in ImageSequence.Iterator(img):
                frame = frame.resize((45, 45), Image.Resampling.LANCZOS)
                frames.append(ImageTk.PhotoImage(frame))
            return frames
        except: return []

    def set_click_through(self, enabled):
        """Update: Click-through dimatikan agar tombol bisa ditekan."""
        hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())
        # GWL_EXSTYLE = -20
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
        if enabled:
            # Tambahkan gaya tembus (WS_EX_TRANSPARENT = 0x20)
            new_style = style | 0x80000 | 0x20
            self.root.attributes("-alpha", 0.4)
        else:
            # Hapus gaya tembus agar bisa diklik (Reset & X)
            new_style = style & ~0x20
            self.root.attributes("-alpha", 1.0) # Solid kembali agar teks jelas
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, new_style)

    def sync_loop(self):
        try:
            active_win = gw.getActiveWindow()
            if active_win and "Word" in active_win.title:
                nx = active_win.left + active_win.width - self.widget_w - 30
                ny = active_win.top + active_win.height - self.widget_h - 40
                self.root.geometry(f"{self.widget_w}x{self.widget_h}+{nx}+{ny}")
                self.root.deiconify()

                mx, my = win32api.GetCursorPos()
                # CEK: Jika kursor di dalam widget, MATIKAN click-through agar tombol bisa diklik
                if (nx <= mx <= nx + self.widget_w) and (ny <= my <= ny + self.widget_h):
                    if self.is_transparent:
                        self.set_click_through(False)
                        self.is_transparent = False
                else:
                    # Jika kursor di luar, AKTIFKAN click-through agar tidak menghalangi Word
                    if not self.is_transparent:
                        self.set_click_through(True)
                        self.is_transparent = True
            else:
                self.root.withdraw()
        except: pass
        self.root.after(100, self.sync_loop)

    def animate_loop(self):
        now = time.time()
        new_gif = 'typing' if now - self.last_type_time < 2.0 else 'wait'
        if new_gif != self.current_gif:
            self.current_gif = new_gif
            self.frame_idx = 0
        frames = self.gif_data[self.current_gif]
        if frames:
            self.frame_idx = (self.frame_idx + 1) % len(frames)
            self.img_label.config(image=frames[self.frame_idx])
        self.root.after(100, self.animate_loop)

    def reset_counter(self):
        self.char_count = 0
        self.start_time = None
        self.wpm_label.config(text="WPM : 00")

    def on_press(self, key):
        active_win = gw.getActiveWindow()
        if active_win and "Word" in active_win.title:
            now = time.time()
            self.last_type_time = now

            if hasattr(key, 'char') or key == keyboard.Key.space:
                self.keypress_times.append(now)

                while self.keypress_times and now - self.keypress_times[0] > 60:
                    self.keypress_times.popleft()

                current_wpm = len(self.keypress_times)/5
            
                self.wpm_label.config(text=f"WPM : {int(current_wpm):02}")


if __name__ == "__main__":
    check_singleton()

    WordFinalOverlay()