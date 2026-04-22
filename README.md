# 🔐 Keylogger (Cybersecurity Project)

A **Python-based Keylogger*** developed as part of B.Tech Industrial Training at **Ardent Computech Pvt. Ltd.*

This project demonstrates **secure keystroke logging with encryption, ethical compliance, and system monitoring techniques**.

---

## 📌 Introduction

A keylogger is a software tool that records keystrokes made by a user. While it has legitimate uses like **parental control, system auditing, and security research**, it can also be misused.

👉 This project focuses on **ethical and secure implementation** of a keylogger.

---

## 🎯 Objectives

* Develop a lightweight keylogger for Linux
* Capture and store keystrokes securely
* Implement **AES encryption**
* Generate reports from logs
* Ensure **ethical and legal compliance**
* Protect user privacy with auto-deletion & secure storage

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * `pynput` (keystroke capture)
  * `cryptography / AES` (encryption)
  * `datetime`, `os`, `threading`

---

## ⚙️ System Workflow

1. Start keylogger
2. Capture keystrokes
3. Add timestamp & context
4. Encrypt data (AES)
5. Store in secure file
6. Auto-delete logs after time
7. Generate reports

---

## 🔐 Security Features

* AES encrypted logs
* Session-based key generation (no key storage)
* Hidden log storage
* Auto log deletion
* Restricted access control

---

## 🧠 Methodology

* Background execution using Python
* Real-time keystroke capture using `pynput`
* Encryption using AES (secure + fast)
* Log storage with timestamped files
* Report generation (CSV/TXT)

---

## 📊 Results & Performance

* ✔️ Accurate keystroke logging
* ✔️ <3% CPU usage
* ✔️ <50MB RAM usage
* ✔️ Real-time logging (<10ms delay)
* ✔️ Encrypted secure storage

---

## ⚠️ Security Analysis

**Threats Addressed:**

* Unauthorized access
* Data leakage
* Log tampering

**Mitigation:**

* AES encryption
* Session keys
* No network transmission
* Auto log deletion

---

## ⚖️ Ethical Considerations

* Must be used **with user consent**
* Unauthorized monitoring is illegal
* Complies with:

  * IT Act (India)
  * GDPR (EU)

---

## 📂 Project Structure

```
keylogger/
├── src/
├── screenshots/
├── reports/
├── docs/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation & Usage

```bash
git clone https://github.com/rohitmaji22/keylogger.git
cd keylogger
pip install -r requirements.txt
python src/keylogger.py
```

---

## 📸 Screenshots

*Add your screenshots here*

```
![Output](screenshots/your-image.png)
```

---

## 🔮 Future Improvements

* Web dashboard (Flask)
* Email alerts
* Log visualization
* ML-based behavior detection

---

## ⚠️ Disclaimer

This project is strictly for **educational and ethical purposes only**.

> Unauthorized use of keyloggers is illegal and punishable under law.

---

## 👨‍💻 Author

**Rohit Maji**
B.Tech (Cyber Security)

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!
