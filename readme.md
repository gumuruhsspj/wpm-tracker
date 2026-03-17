
# 📝 Word WPM Overlay Tracker

A lightweight **Python desktop overlay widget** that tracks your **typing speed (WPM)** in real time while typing in **Microsoft Word**.

The widget automatically appears on top of the Word window and displays your **current Words Per Minute (WPM)** along with a small animated indicator showing whether you're typing or idle.

---

## ✨ Features

* ⌨️ **Real-time WPM tracking** while typing in Microsoft Word
* 🪟 **Floating overlay widget** that follows the Word window
* 🎞 **Animated GIF indicator**

  * `typing.gif` → shown when you are actively typing
  * `wait.gif` → shown when idle
* 🖱 **Smart click-through system**

  * Transparent when not hovered
  * Interactive when mouse is over the widget
* 🔄 **Reset button** to restart WPM calculation
* ❌ **Close button** to exit the overlay
* 🧠 Automatically hides when Word is not the active window

---

## 📸 Preview

Example overlay widget:

```
+--------------------------+
|                    x     |
|  [GIF]   WPM : 72        |
|                reset     |
+--------------------------+
```

The widget appears in the **bottom-right corner of the Microsoft Word window**.

---

## ⚙️ How It Works

The program:

1. Detects the **active window**.
2. If the active window contains **"Word"**, the widget appears.
3. A **keyboard listener** tracks your typing.
4. Characters are counted and converted to **Words Per Minute (WPM)**.

WPM formula used:

```
WPM = (characters / 5) / time_in_minutes
```

(1 word = 5 characters standard typing metric)

---

## 📦 Requirements

Python **3.8+**

Install dependencies:

```bash
pip install pillow pygetwindow pynput pywin32
```

---

## 📁 Project Structure

```
word-wpm-overlay/
│
├── tracker.py
├── typing.gif
├── wait.gif
└── README.md
```

---

## ▶️ Running the Project

Run the script:

```bash
python tracker.py
```

Then:

1. Open **Microsoft Word**
2. Start typing
3. The overlay widget will appear and show your **live WPM**

---

## 🖥 Platform

Currently tested on:

* Windows 10 / 11
* Microsoft Word

The project relies on **Windows APIs**, so it will not work on macOS or Linux.

---

## 🛠 Technologies Used

* **Python**
* Tkinter (GUI overlay)
* Pillow (GIF animation)
* pynput (keyboard listener)
* pygetwindow (active window detection)
* win32api / ctypes (Windows interaction)

---

## 🚀 Future Improvements

Possible upgrades:

* Typing **accuracy tracking**
* **Session statistics**
* Support for **Google Docs / browser typing**
* Save **typing history**
* Custom widget themes

---

## 📜 License

MIT License

---

## 👤 Author

Created by **Gumuruh S**

A small utility built for improving typing speed while writing in Word.

Kalau kamu mau, aku juga bisa bantu bikin:

* **README yang lebih “GitHub viral style”** (pakai badges, screenshot section, dll)
* **nama repo yang lebih catchy**
* **GIF demo untuk README** biar project kamu kelihatan jauh lebih keren di portfolio. 🚀
