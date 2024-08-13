import os
import subprocess
import sys
import time

# Verzeichnis für die Skripte
SCRIPTS_DIRECTORY = 'Lunexa_Library'

# Version des Hauptprogramms
PROGRAM_VERSION = "1.1.2 release"

# ANSI Escape Codes für Farben und Formatierungen
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED = '\033[7m'
    CYAN = '\033[96m'
    MAGENTA = '\033[35m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_GREEN = '\033[92m'
    WHITE = '\033[97m'  # Neu hinzugefügt
    PURPLE = '\033[35m'  # Neu hinzugefügt
    RED = '\033[31m'     # Neu hinzugefügt

def set_terminal_size(columns, rows):
    """Setzt die Terminalgröße für Windows und Unix-basierte Systeme."""
    try:
        if os.name == 'nt':  # Windows
            os.system(f'mode con: cols={columns} lines={rows}')
        else:  # Unix-basierte Systeme
            os.system(f'stty cols {columns} rows {rows}')
    except Exception as e:
        print(f"{Colors.FAIL}Fehler beim Setzen der Terminalgröße: {e}{Colors.ENDC}")

def clear_screen():
    """Löscht den Bildschirm."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Druckt den Header des Menüs mit grafischen Effekten und Version des Hauptprogramms."""
    print(f"{Colors.OKBLUE}{Colors.BOLD}{Colors.UNDERLINE}{title.center(50)}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'=' * 50}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}Version: {PROGRAM_VERSION}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'=' * 50}{Colors.ENDC}")

def show_loading_bar(task_name):
    """Zeigt eine Ladeanimation mit Balken an."""
    bar_length = 40
    print(f"\n{Colors.CYAN}{task_name}...{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{'[' + ' ' * bar_length + ']'}{Colors.ENDC}", end='\r')
    
    for i in range(bar_length + 1):
        time.sleep(0.05)  # Verlangsamung des Ladebalkens
        filled_length = int(bar_length * i // bar_length)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"\r{Colors.OKGREEN}[{bar}]{Colors.ENDC}", end='')
    
    print()  # Neue Zeile nach der Ladeanimation

def list_files():
    """Listet alle Python-Skripte und Textdateien im Verzeichnis auf und kategorisiert sie."""
    try:
        if not os.path.exists(SCRIPTS_DIRECTORY):
            raise FileNotFoundError(f"Das Verzeichnis '{SCRIPTS_DIRECTORY}' wurde nicht gefunden.")
        
        files = [f for f in os.listdir(SCRIPTS_DIRECTORY) if f.endswith('.py') or f.endswith('.txt')]
        files.sort()  # Sortiere die Dateien alphabetisch
        if not files:
            print(f"{Colors.WARNING}Keine Skripte oder Textdateien gefunden.{Colors.ENDC}")
        else:
            print(f"{Colors.OKBLUE}Verfügbare Dateien:{Colors.ENDC}")
            for index, file in enumerate(files, start=1):
                # Bestimme die Farbe basierend auf dem Dateinamen
                if file.startswith('README'):
                    color = Colors.WHITE
                elif file.startswith('auto_'):
                    color = Colors.PURPLE
                elif file.startswith('interactive_'):
                    color = Colors.RED
                else:
                    color = Colors.OKGREEN
                
                print(f"{color}{index}. {file}{Colors.ENDC}")
        return files
    except Exception as e:
        print(f"{Colors.FAIL}Fehler: {e}{Colors.ENDC}")
        return []

def execute_script(script_name, script_type):
    """Führt das angegebene Python-Skript basierend auf seinem Typ aus."""
    script_path = os.path.join(SCRIPTS_DIRECTORY, script_name)
    
    if not os.path.exists(script_path):
        print(f"{Colors.FAIL}Das Skript '{script_name}' wurde nicht gefunden.{Colors.ENDC}")
        return
    
    try:
        if script_type == 'interactive':
            print(f"{Colors.OKBLUE}Führe {script_name} aus...{Colors.ENDC}")
            show_loading_bar(f"Ausführen des Skripts '{script_name}'")
            
            if os.name == 'nt':  # Windows
                subprocess.Popen(['start', 'python', script_path], shell=True)
            else:  # Unix-basierte Systeme
                subprocess.Popen(['gnome-terminal', '--', 'python', script_path])
            
            print(f"{Colors.OKBLUE}Das interaktive Skript '{script_name}' wird in einem neuen Terminalfenster ausgeführt.{Colors.ENDC}")
        
        else:
            print(f"{Colors.OKBLUE}Führe {script_name} aus...{Colors.ENDC}")
            show_loading_bar(f"Ausführen des Skripts '{script_name}'")
            
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            
            if result.stdout:
                print(f"\n{Colors.OKBLUE}Ausgabe des Skripts:{Colors.ENDC}")
                print(result.stdout)
            if result.stderr:
                print(f"{Colors.FAIL}Fehlerausgabe des Skripts:{Colors.ENDC}")
                print(result.stderr)
    
    except Exception as e:
        print(f"{Colors.FAIL}Fehler beim Ausführen des Skripts: {e}{Colors.ENDC}")

def display_text_file(file_name):
    """Zeigt den Inhalt einer Textdatei im Terminal an."""
    file_path = os.path.join(SCRIPTS_DIRECTORY, file_name)
    
    if not os.path.exists(file_path):
        print(f"{Colors.FAIL}Die Datei '{file_name}' wurde nicht gefunden.{Colors.ENDC}")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"{Colors.OKBLUE}Inhalt der Datei '{file_name}':{Colors.ENDC}")
            print(content)
    except Exception as e:
        print(f"{Colors.FAIL}Fehler beim Lesen der Datei: {e}{Colors.ENDC}")

def reboot_program():
    """Startet das Programm neu."""
    print(f"{Colors.WARNING}Neustart des Programms...{Colors.ENDC}")
    time.sleep(1)  # Kleine Verzögerung für den Neustart

    # Einfacher Neustart des Programms
    python = sys.executable
    os.execl(python, python, *sys.argv)

def show_instruction():
    """Zeigt eine Schritt-für-Schritt-Anleitung zur Verwendung des Programms an."""
    clear_screen()
    print_header("Anleitung")
    print(f"{Colors.OKBLUE}Schritt-für-Schritt Anleitung{Colors.ENDC}")

    instructions = [
        "1. Vorbereitungen:",
        "   - Stelle sicher, dass der Ordner 'Lunexa_Library' im selben Verzeichnis wie dieses Programm",
        "     vorhanden ist.",
        "   - Der Ordner sollte Python-Skripte (.py) und/oder Textdateien (.txt) enthalten,",
        "     die du ausführen möchtest",
        "",
        "2. Hauptmenü Navigation:",
        "   - Wähle '1', um alle verfügbaren Skripte und Textdateien im Ordner aufzulisten.",
        "   - Wähle '2', um eine Datei aus der Liste auszuführen.",
        "   - Wähle '3', um das Programm neu zu starten.",
        "   - Wähle '4', um die Anleitung anzuzeigen.",
        "   - Wähle '5', um das Programm zu beenden.",
        "",
        "3. Skriptausführung:",
        "   - Beim Ausführen eines Skripts wird der Name des Skripts angezeigt und die Ausgabe wird im",
        "     Terminal angezeigt.",
        "   - Bei Fehlern wird die Fehlermeldung ebenfalls angezeigt.",
        "",
        "4. Fehlerbehebung:",
        "   - Stelle sicher, dass die Skripte im Verzeichnis korrekt benannt sind und keine Importfehler",
        "     aufweisen.",
        "   - Überprüfe die Terminal-Ausgabe auf spezifische Fehlermeldungen und reagiere entsprechend.",
        "",
        "5. Neustart:",
        "   - Wenn du '3' wählst, wird das Programm neu gestartet, um mögliche Änderungen zu übernehmen."
    ]

    for line in instructions:
        print(f"{Colors.OKGREEN}{line}{Colors.ENDC}")

    input(f"{Colors.OKGREEN}Drücke Enter, um zum Hauptmenü zurückzukehren...{Colors.ENDC}")

def select_and_execute_script():
    """Ermöglicht dem Benutzer, ein Skript aus der Liste auszuwählen und auszuführen."""
    while True:
        files = list_files()
        if files:
            try:
                selection = int(input(f"{Colors.OKGREEN}Gib die Nummer der Datei ein: {Colors.ENDC}").strip())
                if 1 <= selection <= len(files):
                    file_name = files[selection - 1]
                    
                    if file_name.endswith('.py'):
                        # Bestimme den Typ des Skripts
                        if file_name.startswith('interactive_'):
                            execute_script(file_name, 'interactive')
                        else:
                            execute_script(file_name, 'normal')
                    elif file_name.endswith('.txt'):
                        display_text_file(file_name)
                else:
                    print(f"{Colors.WARNING}Ungültige Nummer.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.WARNING}Bitte gib eine gültige Nummer ein.{Colors.ENDC}")
            
            # Frage, ob der Benutzer ein weiteres Skript ausführen möchte
            choice = input(f"{Colors.OKGREEN}Möchtest du ein weiteres Skript ausführen? (j/n): {Colors.ENDC}").strip().lower()
            if choice != 'j':
                break
        else:
            break

def show_main_menu():
    """Zeigt das Hauptmenü an und verarbeitet Benutzereingaben."""
    auto_files = []
    normal_files = []
    interactive_files = []
    
    # Initiales Dateierkennen und Kategorisierung
    try:
        files = list_files()
        for file in files:
            if file.startswith('auto_'):
                auto_files.append(file)
            elif file.startswith('interactive_'):
                interactive_files.append(file)
            elif file.endswith('.txt'):
                normal_files.append(file)
            else:
                normal_files.append(file)
    except Exception as e:
        print(f"{Colors.FAIL}Fehler beim Kategorisieren der Dateien: {e}{Colors.ENDC}")
    
    # Auto-Erweiterungen automatisch ausführen
    for file in auto_files:
        execute_script(file, 'normal')
    
    while True:
        clear_screen()
        print_header("Hauptmenü")
        print(f"{Colors.OKBLUE}1.{Colors.ENDC} {Colors.BOLD}Liste alle Dateien auf{Colors.ENDC}")
        print(f"{Colors.OKBLUE}2.{Colors.ENDC} {Colors.BOLD}Datei ausführen{Colors.ENDC}")
        print(f"{Colors.OKBLUE}3.{Colors.ENDC} {Colors.BOLD}Neustart{Colors.ENDC}")
        print(f"{Colors.OKBLUE}4.{Colors.ENDC} {Colors.BOLD}Anleitung{Colors.ENDC}")
        print(f"{Colors.OKBLUE}5.{Colors.ENDC} {Colors.BOLD}Beenden{Colors.ENDC}")

        choice = input(f"\n{Colors.OKGREEN}Bitte wähle eine Option (1/2/3/4/5): {Colors.ENDC}").strip()

        if choice == '1':
            list_files()
            input(f"\n{Colors.OKGREEN}Drücke Enter, um zum Hauptmenü zurückzukehren...{Colors.ENDC}")
        elif choice == '2':
            select_and_execute_script()  # Hier wird die neue Funktion aufgerufen
            input(f"\n{Colors.OKGREEN}Drücke Enter, um zum Hauptmenü zurückzukehren...{Colors.ENDC}")
        elif choice == '3':
            reboot_program()
        elif choice == '4':
            show_instruction()
        elif choice == '5':
            print(f"{Colors.OKGREEN}Beende das Programm...{Colors.ENDC}")
            time.sleep(1)
            break
        else:
            print(f"{Colors.FAIL}Unbekannte Option. Bitte versuche es erneut.{Colors.ENDC}")

if __name__ == "__main__":
    try:
        # Setzt die Terminalgröße auf eine angenehme Größe
        set_terminal_size(100, 30)
        
        show_main_menu()
    except Exception as e:
        print(f"{Colors.FAIL}Unerwarteter Fehler: {e}{Colors.ENDC}")
        sys.exit(1)
