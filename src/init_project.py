import subprocess
import sys
import os
import shutil
from utils.complete_readme import complete_readme

def init_project(project_type, project_name):    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    file = os.path.join(script_dir, project_type.replace("-", "_") + ".py")
    if not os.path.isfile(file):
        print(f"Project type '{project_type}' does not exist.")
        return
    
    # 1. Create a new dir with the project name and go to it
    if os.path.exists(project_name):
        print(f"Directory '{project_name}' already exists.")
        return
    
    os.makedirs(project_name)
    os.chdir(project_name)
    
    # 3. Coppy readme, license
    current_dir = os.getcwd()
    resources_dir = os.path.join(os.path.dirname(__file__), "..", "resources")
    shutil.copyfile(os.path.join(resources_dir, "README.md"), os.path.join(current_dir, "README.md"))
    shutil.copyfile(os.path.join(resources_dir, "LICENSE"), os.path.join(current_dir, "LICENSE"))
    
     # 4. Modify the readme file
    complete_readme(os.path.join(current_dir, "README.md"), project_name)
    
    # 5. Execute the script with the project name as an argument
    subprocess.run([sys.executable, file, project_name])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect args. Run: python init_project.py <project_type> <project_name>")
    else:
        init_project(sys.argv[1], sys.argv[2])