import shutil
import os
import datetime

# Verzeichnis für Konfigurationsdateien
CONFIG_DIRECTORY = 'Lunexa_Library/Configs'
BACKUP_DIRECTORY = 'Lunexa_Library/Backups'

def backup_config_files():
    """Erstellt Sicherungskopien aller Konfigurationsdateien."""
    if not os.path.exists(BACKUP_DIRECTORY):
        os.makedirs(BACKUP_DIRECTORY)
    
    for file_name in os.listdir(CONFIG_DIRECTORY):
        if file_name.endswith('.conf'):
            src_path = os.path.join(CONFIG_DIRECTORY, file_name)
            now = datetime.datetime.now()
            backup_filename = now.strftime(f"{file_name}_backup_%Y%m%d_%H%M%S.conf")
            dst_path = os.path.join(BACKUP_DIRECTORY, backup_filename)
            shutil.copy2(src_path, dst_path)
            print(f"Sicherungskopie von '{file_name}' erstellt als '{backup_filename}'.")

if __name__ == "__main__":
    backup_config_files()
