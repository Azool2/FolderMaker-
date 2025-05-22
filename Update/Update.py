import subprocess
import os
import shutil

def run_update():
    """
    Klont das aktuelle Projekt von GitHub neu und ersetzt die lokalen Dateien.
    """
    repo_url = "https://github.com/Azool2/FolderMaker-.git"
    try:
        script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    except NameError:
        return False, "__file__ ist nicht definiert."

    tmp_dir = os.path.join(script_dir, "_update_tmp")

    try:
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)

        subprocess.check_call(["git", "clone", repo_url, tmp_dir])

        for item in os.listdir(tmp_dir):
            if item == ".git":
                continue
            src = os.path.join(tmp_dir, item)
            dst = os.path.join(script_dir, item)

            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

        shutil.rmtree(tmp_dir)
        return True, "Update erfolgreich. Bitte neu starten."
    except Exception as e:
        return False, f"Fehler beim Update: {e}"

if __name__ == "__main__":
    success, msg = run_update()
    print(msg)
