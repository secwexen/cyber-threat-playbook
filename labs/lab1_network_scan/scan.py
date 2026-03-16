import socket

def simple_port_scan(target: str, ports: list[int]) -> None:
    print(f"[+] Scanning {target}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
        except Exception:
            pass
        finally:
            s.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1" # Example
    common_ports = [22, 80, 443, 3389]
    simple_port_scan(target_ip, common_ports)
