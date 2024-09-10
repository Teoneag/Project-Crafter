import importlib.util
import subprocess
import sys

def install_missing_packages():
    if importlib.util.find_spec("pyfiglet") is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])

def ascii_art_title(project_name):
    project_name = project_name.replace('-', ' ')
    
    install_missing_packages()
    import pyfiglet
    return pyfiglet.figlet_format(project_name, font = "ansi_shadow", width=110).rstrip()

def complete_readme(readme_path, project_name):
    with open(readme_path, "r+", encoding="utf-8") as file:
        formatted_content = file.read().format(ascii_art_title(project_name), project_name)
        file.seek(0)
        file.write(formatted_content)
        file.truncate()