import os  # Importiert das Modul für Betriebssystem-Funktionen (z.B. Ordner erstellen)
import tkinter as tk  # Importiert das tkinter-Modul für die GUI-Erstellung und gibt ihm das Kürzel 'tk'
from tkinter import messagebox  # Importiert das Modul für Popup-Nachrichtenfenster

def create_folders():
    # Holt den eingegebenen Wert aus dem Eingabefeld (Blocknummer)
    block_number = entry.get()
    # Prüft, ob eine Blocknummer eingegeben wurde
    if not block_number:
        # Zeigt eine Warnung an, wenn das Feld leer ist
        messagebox.showwarning("Fehler", "Bitte eine Blocknummer eingeben.")
        return

    # Setzt den Basis-Pfad (hier: Desktop des aktuellen Benutzers)
    base_path = os.path.expanduser("~/Desktop")  # z. B. Desktop
    # Erstellt den Namen des Hauptordners mit der Blocknummer
    folder_name = f"Block_{block_number}"
    # Erstellt den vollständigen Pfad zum Hauptordner
    main_folder = os.path.join(base_path, folder_name)
    # Prüft, ob der Hauptordner bereits existiert
    if os.path.exists(main_folder):
        messagebox.showinfo("Hinweis", f"Ordner '{folder_name}' bereits vorhanden!")
        return
    # Liste der Unterordner, die erstellt werden sollen
    subfolders = ["Footage", "Export", "Project", "_ORGA"]

    try:
        # Erstellt den Hauptordner (exist_ok=True verhindert Fehler, falls er schon existiert)
        os.makedirs(main_folder, exist_ok=True)
        # Erstellt die Unterordner im Hauptordner
        for folder in subfolders:
            os.makedirs(os.path.join(main_folder, folder), exist_ok=True)
        # Zusätzliche Unterordner in Export/Intermediate/Armin, Carsten, Mikko
        intermediate_path = os.path.join(main_folder, "Export", "Intermediate")
        os.makedirs(intermediate_path, exist_ok=True)
        for name in ["Armin", "Carsten", "Mikko"]:
            os.makedirs(os.path.join(intermediate_path, name), exist_ok=True)
        # Zusätzliche Unterordner in Footage/Auto, Done, Template
        footage_path = os.path.join(main_folder, "Footage")
        for sub in ["Auto", "Done", "Template"]:
            os.makedirs(os.path.join(footage_path, sub), exist_ok=True)
        # In Footage/Auto noch CCR anlegen
        auto_ccr_path = os.path.join(footage_path, "Auto", "CCR")
        os.makedirs(auto_ccr_path, exist_ok=True)
        # Zusätzliche Unterordner in Project: AE, PR, PS-AI
        project_path = os.path.join(main_folder, "Project")
        for sub in ["AE", "PR", "PS-AI"]:
            os.makedirs(os.path.join(project_path, sub), exist_ok=True)
        # Zusätzliche Unterordner in _ORGA: Documents, Material
        orga_path = os.path.join(main_folder, "_ORGA")
        documents_path = os.path.join(orga_path, "Documents")
        material_path = os.path.join(orga_path, "Material")
        os.makedirs(documents_path, exist_ok=True)
        os.makedirs(material_path, exist_ok=True)
        # In Documents: Drehbuch, Excel Tabelen
        for sub in ["Drehbuch", "Excel Tabelen"]:
            os.makedirs(os.path.join(documents_path, sub), exist_ok=True)
        # Zeigt eine Erfolgsmeldung an, wenn alles geklappt hat
        # messagebox.showinfo("Erfolg", f"Ordner '{folder_name}' wurde erstellt.")
    except Exception as e:
        # Zeigt eine Fehlermeldung an, falls etwas schiefgeht
        messagebox.showerror("Fehler", str(e))

# GUI erstellen
root = tk.Tk()  # Erstellt das Hauptfenster der Anwendung
root.title("Ordnerstruktur erstellen")  # Setzt den Fenstertitel

# Erstellt ein Label (Textfeld) für die Eingabeaufforderung
tk.Label(root, text="Blocknummer eingeben:").pack(pady=5)
# Erstellt das Eingabefeld für die Blocknummer
entry = tk.Entry(root)
entry.pack(pady=5)
entry.focus_set()
# Bindet die Enter-Taste an die Funktion create_folders
entry.bind('<Return>', lambda event: create_folders())

# Erstellt einen Button, der beim Klicken die Funktion create_folders ausführt
tk.Button(root, text="Ordner erstellen", command=create_folders).pack(pady=10)

root.mainloop()  # Startet die GUI und wartet auf Benutzeraktionen
