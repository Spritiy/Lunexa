# system_info.py

import platform
import socket

def get_system_info():
    """Gibt grundlegende Systeminformationen aus."""
    system_info = {
        "System": platform.system(),
        "Version": platform.version(),
        "Release": platform.release(),
        "Architecture": platform.architecture()[0],
        "Machine": platform.machine(),
        "Node": platform.node(),
        "IP-Adresse": socket.gethostbyname(socket.gethostname())
    }

    return system_info

def main():
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
