# Scenario: PowerShell Execution (T1059)

## Description

Simulated malicious PowerShell execution designed to demonstrate command execution detection, investigation, and response in a controlled lab environment.

**MITRE ATT&CK Technique:** T1059 - Command and Scripting Interpreter  
**Adversary Profile:** APT-like actor executing remote commands via PowerShell

## Objectives

- Demonstrate how PowerShell-based attacks can be detected
- Correlate logs with Sigma detection rules
- Perform investigation and response workflow

## Lab Setup

- Windows 10 / Windows Server machine
- Sysmon installed and configured
- Logging enabled for Event IDs 1, 4688, 4104
- Optional: SIEM / ELK stack for alert visualization

## Attack Simulation

1. Execute encoded PowerShell command:
```powershell
powershell.exe -EncodedCommand <base64_payload>
```

2. Observe process creation and network activity
3. Optional: simulate lateral movement using SMB or WMI

## Detection

- **Sigma Rule:** `sigma_powershell_exec.yml`
- **YARA Rule:** `yara_powershell_payload.yar`
- **Suricata Rule:** N/A (network-based detection optional)
- **Log Source:** Sysmon Event ID 1 (ProcessCreate), Event ID 4688 (Windows Security), Event ID 4104 (PowerShell Script Block Logging)

### Expected Alert

- Detection triggered on encoded command execution
- Parent process suspicious (e.g., `explorer.exe` launching `powershell.exe`)

## Triage

1. Verify parent process legitimacy
2. Confirm user context and logon session
3. Check if script block logging contains unusual patterns

## Investigation

1. Correlate with other endpoint logs
2. Check for lateral movement attempts (SMB/WMI)
3. Review recent logon activity for the affected user
4. Optional: examine network traffic for unusual connections

## Response

1. Kill malicious PowerShell process
2. Isolate affected endpoint from network
3. Review and revoke any compromised credentials
4. Update detection rules with indicators found

## References

- MITRE ATT&CK: [T1059](https://attack.mitre.org/techniques/T1059/)
- Sigma Project: [PowerShell Execution](https://github.com/SigmaHQ/sigma)

## Notes

- This scenario is safe for lab environments only
- Do **not** run in production
- Ensure all telemetry sources are enabled for full detection
