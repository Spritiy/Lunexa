import socket
import psutil
from datetime import datetime

def auto_network_info():
    """Zeigt Netzwerkverbindungsinformationen automatisch an."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    network_info = f"""
    Netzwerkverbindungsinformationen:
    Hostname: {hostname}
    IP-Adresse: {ip_address}
    """
    
    # Netzwerkschnittstellen
    interfaces = psutil.net_if_addrs()
    interface_details = "\n".join(
        f"{iface}: {', '.join(f'{addr.address} ({addr.family})' for addr in addrs)}"
        for iface, addrs in interfaces.items()
    )
    
    network_info += f"\nNetzwerkschnittstellen:\n{interface_details}"
    
    print(network_info)
    with open("network_info_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}\n{network_info}\n")

if __name__ == "__main__":
    auto_network_info()
