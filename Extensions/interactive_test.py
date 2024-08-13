import time

def run_interactive_test():
    """Führt eine interaktive Test-Erweiterung aus."""
    print("Willkommen zur interaktiven Test-Erweiterung!\n")
    
    # Eingaben vom Benutzer sammeln
    name = input("Wie heißt du? ")
    print(f"Hallo, {name}! Schön, dich kennenzulernen.\n")

    age = input("Wie alt bist du? ")
    if age.isdigit():
        print(f"Du bist {age} Jahre alt.\n")
    else:
        print("Das war keine gültige Zahl.\n")

    print("Danke für deine Antworten! Wir hoffen, dir hat die kleine Interaktion gefallen.\n")

if __name__ == "__main__":
    run_interactive_test()
