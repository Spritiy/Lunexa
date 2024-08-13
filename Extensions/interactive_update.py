import os
import requests
import zipfile
import shutil
import sys

# URL der ZIP-Datei zum Herunterladen
DOWNLOAD_URL = 'https://github.com/deinbenutzername/deinrepository/archive/refs/heads/main.zip'

# Verzeichnis für die Erweiterungen
SCRIPTS_DIRECTORY = 'Lunexa_Library'

def validate_url(url):
    """Überprüft, ob die URL auf eine ZIP-Datei verweist."""
    if not url.lower().endswith('.zip'):
        raise ValueError("Die URL muss auf eine ZIP-Datei verweisen.")
    return url

def download_file(url, local_filename):
    """Lädt eine Datei von einer URL herunter und zeigt den Fortschritt an."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Überprüft, ob der Download erfolgreich war

        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        chunk_size = 8192  # 8 KB

        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    done = int(50 * downloaded_size / total_size)
                    sys.stdout.write(f"\r[{'█' * done}{'.' * (50 - done)}] {done * 2}%")
                    sys.stdout.flush()

        print("\nDownload abgeschlossen: {}".format(local_filename))
    except requests.RequestException as e:
        raise RuntimeError(f"Fehler beim Herunterladen der Datei: {e}")

def extract_zip(zip_path, extract_to):
    """Entpackt eine ZIP-Datei."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("Entpacken abgeschlossen: {}".format(extract_to))
    except zipfile.BadZipFile:
        raise RuntimeError("Die ZIP-Datei ist beschädigt oder ungültig.")
    except Exception as e:
        raise RuntimeError(f"Fehler beim Entpacken der Datei: {e}")

def safe_copy(src, dest):
    """Kopiert eine Datei sicher von src nach dest und überschreibt sie, falls erforderlich."""
    try:
        if os.path.isfile(src):
            shutil.copy2(src, dest)
            print(f"Datei kopiert: {src} -> {dest}")
    except IOError as e:
        raise RuntimeError(f"Fehler beim Kopieren der Datei {src}: {e}")

def user_confirmation(prompt):
    """Fragt den Benutzer um Bestätigung mit 'Ja' oder 'Nein'."""
    while True:
        response = input(f"{prompt} (Ja/Nein): ").strip().lower()
        if response in ('ja', 'j'):
            return True
        elif response in ('nein', 'n'):
            return False
        else:
            print("Bitte gib 'Ja' oder 'Nein' ein.")

def main():
    """Hauptfunktion zum Ausführen der Update-Erweiterung."""
    try:
        # URL der ZIP-Datei validieren
        validate_url(DOWNLOAD_URL)
        
        # Temporäre Datei für den Download
        temp_zip = 'temp_download.zip'
        
        # Herunterladen der Datei
        print("Starte Download...")
        download_file(DOWNLOAD_URL, temp_zip)
        
        # Extrahieren des ZIP-Archivs
        extract_dir = 'temp_extracted'
        print("Starte Entpacken...")
        extract_zip(temp_zip, extract_dir)
        
        # Überprüfen und Ersetzen von vorhandenen Erweiterungen
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                source_path = os.path.join(root, file)
                dest_path = os.path.join(SCRIPTS_DIRECTORY, file)
                print(f"Ersetze oder füge hinzu: {source_path} -> {dest_path}")
                safe_copy(source_path, dest_path)
        
        # Bereinigen der temporären Dateien und Verzeichnisse
        shutil.rmtree(extract_dir)
        os.remove(temp_zip)
        
        print("Update abgeschlossen!")
        
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()
