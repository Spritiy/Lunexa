import socket

def get_network_info():
    """Gibt grundlegende Netzwerkdetails ohne externe Bibliotheken aus."""
    try:
        # IP-Adresse
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        print("\033[94m=== Netzwerk-Informationen ===\033[0m")
        
        # IP-Adresse ausgeben
        print("\033[92mIP-Adresse:\033[0m")
        print(f"Hostname: {hostname}")
        print(f"IP-Adresse: {ip_address}")
        
        print("\033[94m=== Ende der Netzwerk-Informationen ===\033[0m")
        
    except Exception as e:
        print(f"\033[91mEin Fehler ist aufgetreten: {e}\033[0m")

if __name__ == "__main__":
    get_network_info()
