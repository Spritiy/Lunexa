# normal_disk_usage.py
import shutil

def get_disk_usage(path):
    """Zeigt die Festplattennutzung für das angegebene Verzeichnis an."""
    total, used, free = shutil.disk_usage(path)
    print(f"Festplattenspeicher für '{path}':")
    print(f"  Gesamt: {total // (2**30)} GiB")
    print(f"  Verwendet: {used // (2**30)} GiB")
    print(f"  Frei: {free // (2**30)} GiB")

if __name__ == "__main__":
    path_to_check = '/'  # Ersetze durch das Verzeichnis, dessen Nutzung du überprüfen möchtest
    get_disk_usage(path_to_check)
