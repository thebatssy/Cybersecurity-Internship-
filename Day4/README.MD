Task: Setup and Use a Firewall on Windows

Tools Used: Windows Defender Firewall (GUI and Command Line via PowerShell)

Steps Performed:

1. Opened Windows Defender Firewall with Advanced Security.
2. Viewed and listed current inbound/outbound firewall rules.
3. Created a new inbound rule to block TCP port 23 (Telnet).
4. Verified the block using Telnet client (`telnet 127.0.0.1 23`) - connection failed.
5. Added a rule to allow port 22 (SSH) for demonstration.
6. Removed the Telnet block rule to restore original state.
7. Documented all commands and screenshots used.

Summary:
Firewalls act as a filter between your device and the internet. They allow or block traffic based on rules. Blocking Telnet (port 23) is a common security step, as Telnet sends data in plain text. This task helps in understanding inbound/outbound traffic and managing rules to harden system security.
