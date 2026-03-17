
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

Download the ready-to-use version:

🔗 [https://fgroupindonesia.com/download/wpm-tracker-tool/](https://fgroupindonesia.com/download/wpm-tracker-tool/)

---

## ✨ Features

* ⌨️ **Real-time WPM tracking** while typing in Microsoft Word
* 🪟 **Floating overlay widget** that follows the Word window
* 🎞 **Animated GIF indicator**

  * `typing.gif` → shown when actively typing
  * `wait.gif` → shown when idle
* 🖱 **Smart click-through system**

  * Transparent when not hovered
  * Interactive when hovered
* 🔄 **Reset button** to restart WPM calculation
* ❌ **Close button** to exit the overlay
* 🧠 Automatically hides when Word is not the active window

---

## 📸 Preview

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

1. Detects the **active window**
2. If the active window contains **"Word"**, the widget appears
3. A **global keyboard listener** tracks your typing
4. Characters are counted and converted into **Words Per Minute (WPM)**

**Formula:**

```
WPM = (characters / 5) / time_in_minutes
```

> Standard assumption: **1 word = 5 characters**

---

## 📦 Requirements

* Python **3.8+**

Install dependencies:

```bash
pip install pillow pygetwindow pynput pywin32 winotify
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

```bash
python tracker.py
```

Then:

1. Open **Microsoft Word**
2. Start typing
3. The overlay widget will appear and display your **live WPM**

---

## 🖥 Platform

Tested on:

* Windows 10 / 11
* Microsoft Word

⚠️ This project relies on **Windows APIs**, so it is **not compatible with macOS or Linux**.

---

## 🛠 Technologies Used

### 🧩 Core

* **Python**

### 🎨 UI

* `tkinter` — GUI framework for creating the overlay window

### 🖥️ System Integration (Windows API)

* `pygetwindow` — Detect active window (Microsoft Word)
* `pywin32` (`win32api`, `win32event`, `winerror`) — Windows API interaction (mutex, cursor, etc.)
* `ctypes` — Low-level Windows API access (click-through & transparency)

### ⌨️ Input Handling

* `pynput` — Global keyboard listener for tracking typing input

### 🖼️ Media

* `Pillow (PIL)` — GIF loading and animation (typing / idle states)

### 🔔 Notifications

* `winotify` — Windows toast notifications

### 📦 Packaging

* `PyInstaller` — Convert Python script into a Windows executable (`.exe`)

---

## 🙏 Credits

Supported by **FGroupIndonesia**
GitHub: [https://github.com/fgroupindonesia](https://github.com/fgroupindonesia)

---

## 📜 License

MIT License

---

## 👤 Author

Created by **Gumuruh S**

A simple utility built to help improve typing speed while writing in Microsoft Word.

---
