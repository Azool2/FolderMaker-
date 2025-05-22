import tkinter as tk  # Importiert das tkinter-Modul für die GUI-Erstellung
from tkinter import messagebox  # Importiert das Modul für Popup-Nachrichtenfenster
import os  # Importiert das Modul für Betriebssystem-Funktionen (z.B. Ordner erstellen)

def start_ui():
    def create_folders():
        block_number = entry.get()  # Holt den eingegebenen Wert aus dem Eingabefeld (Blocknummer)
        pfad = pfad_var.get()  # Holt den ausgewählten Pfad aus den Radiobuttons
        if not block_number:
            messagebox.showwarning("Fehler", "Bitte eine Blocknummer eingeben.")  # Zeigt eine Warnung an, wenn das Feld leer ist
            return
        # Setzt den Basis-Pfad je nach Auswahl
        if pfad == "GZSZ":
            base_path = r"W:\\Shows\\GZSZ"
        elif pfad == "UU":
            base_path = r"W:\\Shows\\UU"
        else:
            base_path = os.path.expanduser("~/Desktop")
        folder_name = f"Block_{block_number}"  # Erstellt den Namen des Hauptordners mit der Blocknummer
        main_folder = os.path.join(base_path, folder_name)  # Erstellt den vollständigen Pfad zum Hauptordner
        subfolders = ["Footage", "Export", "Project", "_ORGA"]  # Liste der Unterordner, die erstellt werden sollen
        if os.path.exists(main_folder):
            messagebox.showinfo("Hinweis", f"Ordner '{folder_name}' bereits vorhanden!")  # Zeigt eine Info, wenn der Ordner schon existiert
            root.destroy()  # Schließt das Fenster
            return
        try:
            os.makedirs(main_folder, exist_ok=True)  # Erstellt den Hauptordner
            for folder in subfolders:
                os.makedirs(os.path.join(main_folder, folder), exist_ok=True)  # Erstellt die Unterordner
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
            messagebox.showinfo("Erfolg", f"Ordner '{folder_name}' wurde erstellt.")  # Zeigt eine Erfolgsmeldung an
            root.destroy()  # Schließt das Fenster
        except Exception as e:
            messagebox.showerror("Fehler", str(e))  # Zeigt eine Fehlermeldung an, falls etwas schiefgeht
            root.destroy()  # Schließt das Fenster

    root = tk.Tk()  # Erstellt das Hauptfenster der Anwendung
    root.title("Ordnerstruktur erstellen")  # Setzt den Fenstertitel
    window_width = 350  # Breite des Fensters
    window_height = 180  # Höhe des Fensters
    screen_width = root.winfo_screenwidth()  # Bildschirmbreite ermitteln
    screen_height = root.winfo_screenheight()  # Bildschirmhöhe ermitteln
    x = int((screen_width / 2) - (window_width / 2))  # X-Position für zentriertes Fenster
    y = int((screen_height / 2) - (window_height / 2))  # Y-Position für zentriertes Fenster
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Positioniert das Fenster mittig
    tk.Label(root, text="Blocknummer eingeben:").pack(pady=5)  # Label für die Eingabeaufforderung
    entry = tk.Entry(root)  # Eingabefeld für die Blocknummer
    entry.pack(pady=5)
    entry.focus_set()  # Setzt den Fokus auf das Eingabefeld
    pfad_var = tk.StringVar(value="GZSZ")  # Variable für die Radiobutton-Auswahl, Standard: GZSZ
    frame = tk.Frame(root)  # Frame für die Radiobuttons
    frame.pack(pady=5)
    tk.Radiobutton(frame, text="GZSZ", variable=pfad_var, value="GZSZ").pack(side="left", padx=5)  # Radiobutton GZSZ
    tk.Radiobutton(frame, text="UU", variable=pfad_var, value="UU").pack(side="left", padx=5)  # Radiobutton UU
    tk.Radiobutton(frame, text="Desktop", variable=pfad_var, value="Desktop").pack(side="left", padx=5)  # Radiobutton Desktop
    entry.bind('<Return>', lambda event: create_folders())  # Enter-Taste löst die Funktion aus
    root.bind('<Escape>', lambda event: root.destroy())  # Escape-Taste schließt das Fenster
    tk.Button(root, text="Ordner erstellen", command=create_folders).pack(pady=10)  # Button zum Erstellen der Ordner
    root.mainloop()  # Startet die GUI und wartet auf Benutzeraktionen
