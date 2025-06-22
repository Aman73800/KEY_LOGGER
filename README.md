# 🛡️ Python Keylogger (Educational Use Only)

A simple keylogger built using Python's `pynput` library. This project demonstrates how to monitor keyboard input and log keystrokes to a file with timestamps.

> ⚠️ **Disclaimer:** This keylogger is created strictly for **educational and ethical purposes only**. Never use keyloggers without proper authorization, as doing so may violate privacy laws and ethical standards.

---

## 📁 Features

* Records all keystrokes (letters, numbers, symbols).
* Logs special keys (e.g., `Enter`, `Space`, `Shift`).
* Saves logs to a `logs/` directory with a timestamped filename.
* Automatically stops on pressing the `ESC` key.

---

## 🧰 Requirements

* Python 3.6+
* `pynput` library

Install dependencies:

```bash
pip install pynput
```

---

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aman73800/Python-Keylogger.git
   cd Python-Keylogger
   ```

2. **Run the script:**

   ```bash
   python keylogger.py
   ```

3. **Watch it work:**

   * A message `"Keylogger started. Press ESC to stop."` will appear.
   * Every key you press will be saved in a file inside the `logs/` folder.
   * Press the `ESC` key to stop the keylogger.

---

## 📂 Output Example

The log file will be saved with a name like:

```
logs/keylog_20250622_123456.txt
```

Sample content:

```
2025-06-22 12:35:01,328: Key pressed: a
2025-06-22 12:35:02,045: Special key pressed: Key.space
```

---

## 🔐 Important Notes

* Do **not** use this on devices or systems without explicit permission.
* Useful for understanding how keyboard hooks work for ethical hacking and cybersecurity training.
* Avoid uploading sensitive log data to public repositories.

---

## 📸 Screenshots

> See the `/screenshots` folder or LinkedIn post for visuals of:

* Directory structure
* Script execution
* Log file output
* Example keystroke logs

---

## 🧠 Learning Goals

* Keyboard event handling using `pynput`.
* Working with file systems in Python.
* Using `datetime` and `logging` for efficient log management.
* Awareness of ethical practices in software development.

---

## 📌 License

This project is open for learning and demo purposes under the MIT License.

---

## 📬 Contact

Made by [Aman Yadav](https://www.linkedin.com/in/aman73800/).
Feel free to connect and discuss more such Python experiments!
