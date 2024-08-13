import os
import datetime

# Verzeichnis für die Log-Dateien
LOG_DIRECTORY = 'Lunexa_Library/Logs'

def create_log_file():
    """Erstellt eine Log-Datei mit dem aktuellen Datum und der Uhrzeit."""
    now = datetime.datetime.now()
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)
    filename = now.strftime("log_%Y%m%d_%H%M%S.txt")
    file_path = os.path.join(LOG_DIRECTORY, filename)

    with open(file_path, 'w') as file:
        file.write(f"Log-Datei erstellt am: {now.strftime('%d.%m.%Y %H:%M:%S')}\n")
        file.write("Dies ist eine automatisch erstellte Log-Datei.\n")
    
    print(f"Log-Datei '{filename}' wurde im Verzeichnis '{LOG_DIRECTORY}' erstellt.")

if __name__ == "__main__":
    create_log_file()
