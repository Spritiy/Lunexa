import os

# Erforderliche Verzeichnisse
REQUIRED_DIRECTORIES = ['Lunexa_Library/Logs', 'Lunexa_Library/Reports']

def check_and_create_directories():
    """Überprüft und erstellt erforderliche Verzeichnisse."""
    for directory in REQUIRED_DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Verzeichnis '{directory}' wurde erstellt.")
        else:
            print(f"Verzeichnis '{directory}' existiert bereits.")

if __name__ == "__main__":
    check_and_create_directories()
