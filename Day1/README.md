# 🔍 Cybersecurity Internship – Day 1 Task

## ✅ Task: Scan Your Local Network for Open Ports

---

## 🎯 Objective:
Use **Nmap** to perform a TCP SYN scan on your local network (`192.168.0.0/24`), identify devices and open ports, analyze potential risks, and answer related interview questions.

---

## 🛠 Tools Used:
- **Nmap** (Network Mapper)
- Platform: Windows 11 PC
- Command Line / Terminal

---

## 🖥 Command Used:
```bash
nmap -sS 192.168.0.0/24 

sS → TCP SYN scan (stealth mode)
24 → Scans entire subnet of 192.168.0.1 to 192.168.0.254
