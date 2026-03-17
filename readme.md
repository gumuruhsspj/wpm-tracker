
---

# 📝 Word WPM Overlay Tracker

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

A lightweight **Python desktop overlay widget** that tracks your **typing speed (WPM)** in real time while typing in **Microsoft Word**.

The widget automatically appears on top of the Word window and displays your **current Words Per Minute (WPM)** along with a small animated indicator showing whether you're typing or idle.

---

## ⬇️ Download

If you want to download the ready-to-use version:

🔗 [https://fgroupindonesia.com/download/wpm-tracker-tool/](https://fgroupindonesia.com/download/wpm-tracker-tool/)

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

1. Detects the **active window**
2. If the active window contains **"Word"**, the widget appears
3. A **keyboard listener** tracks your typing
4. Characters are counted and converted to **Words Per Minute (WPM)**

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

## 🙏 Credits

This project is supported by **FGroupIndonesia**.

GitHub organization:
[https://github.com/fgroupindonesia](https://github.com/fgroupindonesia)

---

## 📜 License

MIT License

---

## 👤 Author

Created by **Gumuruh S**

A small utility built for improving typing speed while writing in Word.

---

✅ **Kesimpulan:**
README kamu **sudah benar**, cuma aku tambahkan:

* section **Download**
* section **Credits**
* formatting lebih GitHub-friendly
* link FGroupIndonesia lebih jelas

---
