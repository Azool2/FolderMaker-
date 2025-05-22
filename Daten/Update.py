import subprocess
import sys
import os

def run_update():
    """
    Lädt das aktuelle Projekt von GitHub neu herunter und ersetzt die lokalen Dateien.
    """
    repo_url = "https://github.com/Azool2/FolderMaker-.git"
    script_dir = os.path.dirname(os.path.dirname(__file__))  # Wurzelverzeichnis (eine Ebene über Daten)
    tmp_dir = os.path.join(script_dir, "_update_tmp")
    try:
        # 1. Temporäres Verzeichnis ggf. löschen
        if os.path.exists(tmp_dir):
            import shutil
            shutil.rmtree(tmp_dir)
        # 2. Repo klonen
        subprocess.check_call([sys.executable, "-m", "git", "clone", repo_url, tmp_dir])
        # 3. Dateien (außer .git und _update_tmp) ins Hauptverzeichnis kopieren
        import shutil
        for item in os.listdir(tmp_dir):
            if item == ".git":
                continue
            s = os.path.join(tmp_dir, item)
            d = os.path.join(script_dir, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        # 4. Temporäres Verzeichnis löschen
        shutil.rmtree(tmp_dir)
        return True, "Update erfolgreich! Bitte die Anwendung neu starten."
    except Exception as e:
        return False, f"Update fehlgeschlagen: {e}"