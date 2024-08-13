# Anleitung zu den Erweiterungen

## Übersicht

In diesem Programm können Sie drei Hauptarten von Erweiterungen verwenden:

### 1. Auto-Erweiterungen

**Funktionsweise:**
Auto-Erweiterungen werden automatisch beim Start des Hauptprogramms ausgeführt. Sie führen Aufgaben durch, die ohne Benutzereingriffe erledigt werden sollen, wie das Sammeln von Systeminformationen oder das Erstellen von Log-Dateien.

**Wichtige Hinweise:**
- Diese Erweiterungen sollten keine zeitintensiven Aufgaben durchführen, um die Startzeit des Hauptprogramms nicht zu verlängern.
- Sie sollten keine sensiblen Daten loggen oder speichern, es sei denn, dies ist notwendig.

### 2. Interaktive Erweiterungen

**Funktionsweise:**
Interaktive Erweiterungen werden manuell über das Menü des Hauptprogramms gestartet. Sie erfordern direkte Interaktion vom Benutzer, wie das Suchen nach Dateien oder das Bearbeiten von Inhalten.

**Wichtige Hinweise:**
- Diese Erweiterungen sollten klare Eingabeaufforderungen bieten und keine irreversiblen Änderungen vornehmen, ohne den Benutzer zu warnen.
- Testen Sie diese Erweiterungen gründlich, um Fehler und Datenverluste zu vermeiden.

