import os

def interactive_file_operations():
    """Ermöglicht dem Benutzer das Erstellen, Löschen und Umbenennen von Dateien."""
    print("1. Datei erstellen")
    print("2. Datei löschen")
    print("3. Datei umbenennen")
    choice = input("Wähle eine Option (1/2/3): ").strip()
    
    if choice == '1':
        filename = input("Gib den Namen der zu erstellenden Datei ein: ")
        with open(filename, 'w') as file:
            file.write("")
        print(f"Datei '{filename}' wurde erstellt.")
    
    elif choice == '2':
        filename = input("Gib den Namen der zu löschenden Datei ein: ")
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Datei '{filename}' wurde gelöscht.")
        else:
            print("Datei nicht gefunden.")
    
    elif choice == '3':
        old_name = input("Gib den aktuellen Namen der Datei ein: ")
        new_name = input("Gib den neuen Namen der Datei ein: ")
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"Datei umbenannt von '{old_name}' zu '{new_name}'.")
        else:
            print("Datei nicht gefunden.")
    
    else:
        print("Ungültige Auswahl.")

if __name__ == "__main__":
    interactive_file_operations()
