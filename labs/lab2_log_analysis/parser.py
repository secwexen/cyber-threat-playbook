import json
from pathlib import Path

LOG_FILE = Path("malware_log_example.txt")

def parse_log_line(line: str) -> dict | None:
    line = line.strip()
    if not line:
        return None
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return None

def main() -> None:
    if not LOG_FILE.exists():
        print(f"[!] Log file not found: {LOG_FILE}")
        return

    print(f"[+] Parsing log file: {LOG_FILE}")
    suspicious = []

    with LOG_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            entry = parse_log_line(line)
            if not entry:
                continue

            if entry.get("severity") == "high":
                suspicious.append(entry)

    print(f"[+] Found {len(suspicious)} suspicious entries")
    for s in suspicious:
        print(f"- {s.get('timestamp')} | {s.get('event')} | {s.get('severity')}")

if __name__ == "__main__":
    main()
