# Run Commands

## Sigma Rules

Sigma rules do not run directly.  
They are used inside SIEM platforms (Splunk, Elastic, Wazuh, etc.).

## Suricata Rule

Test Suricata rules:
```
sudo suricata -T -c /etc/suricata/suricata.yaml
```

## YARA Rule

```
yara malware_sample.yar testfile.exe
```

## Port Scan Script

```
python scan.py
```

## Log Parser Script

```
python parser.py
```

## Sigma Parser Script

```
python sigma_parser.py
```

## Log File

Used automatically by parser.py:
```
malware_log_example.txt
```
