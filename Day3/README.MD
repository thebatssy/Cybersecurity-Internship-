# Cyber Security Internship – Day 3

**Task**: Perform a Basic Vulnerability Scan on Your PC

- **Tool Used**: Nessus Essentials  
- **System**: Windows 11
- **Scan Target**: Localhost (`192.168.1.5`)

## Steps Followed
1. Installed **Nessus Essentials** on Windows 11.  
2. Set scan target to local IP `192.168.1.5`.  
3. Performed a full vulnerability scan.  
4. Waited ~45 minutes for scan to complete.  
5. Reviewed report for vulnerabilities.  
6. Documented and researched key issues.  
7. Saved results in text format.

## Key Findings
- **SMBv1 Protocol Enabled** (CVE-2017-0144) – *Critical*  
  _Fix:_ Disable SMBv1 via Windows Features.
- **TLS 1.0 Support Detected** – *High*  
  _Fix:_ Disable TLS 1.0, enable TLS 1.2+.
- **Outdated Google Chrome** – *Medium*  
  _Fix:_ Update to latest stable version.

## Files Included
- `scan_report.txt` – Full vulnerability scan results.  
- `vulnerabilities_summary.txt` – Summary of top-3 vulnerabilities. 
