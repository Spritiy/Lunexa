import os

# Fehlerhafte Funktion zum Anzeigen von Fehlercodes
def display_error_codes_with_errors():
    """Zeigt Fehlercodes an, enthält aber absichtliche Fehler."""
    # Fehlerhafte Fehlercodes-Daten (fehlerhafte Struktur)
    error_codes = {
        1: "Dateipfad nicht gefunden.",
        2: "Fehler beim Ausführen des Skripts.",
        3: "Fehler beim Lesen der Datei.",
        4: "Unerwarteter Fehler.",
        5: "Unbekannter Fehler"  # Fehlerhafte Fehlercodes-Struktur
    }
    
    # Versuche, auf ein nicht existierendes Element zuzugreifen (absichtlicher Fehler)
    try:
        for code, description in error_codes.items():
            if code == 5:
                raise KeyError("Absichtlicher Fehler: Key 5 nicht vorhanden")
            print(f"Code {code}: {description}")
    except KeyError as e:
        print(f"Fehler aufgetreten: {e}")
    
    # Versuche, eine nicht definierte Variable zu verwenden (absichtlicher Fehler)
    try:
        print(f"Unbekannter Code: {undefined_variable}")  # absichtlicher Fehler
    except Exception as e:
        print(f"Fehler beim Anzeigen des unbekannten Codes: {e}")

if __name__ == "__main__":
    display_error_codes_with_errors()
