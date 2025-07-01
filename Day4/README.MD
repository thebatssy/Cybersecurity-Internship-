# Day 4 - Windows Firewall Setup and Usage

## 🛠️ Task: Setup and Use a Firewall on Windows

### 🔧 Tools Used:
- **Windows Defender Firewall** (GUI)
- **PowerShell** (Command Line)

---

## 🧾 Steps Performed:

1. **Opened** Windows Defender Firewall with Advanced Security.
2. **Viewed and listed** current inbound and outbound firewall rules.
3. **Created a new inbound rule** to **block TCP port 23 (Telnet)**:
   - Protocol: TCP  
   - Port: 23  
   - Action: Block the connection
4. **Verified the block** using Telnet client:
   ```powershell
   telnet 127.0.0.1 23
