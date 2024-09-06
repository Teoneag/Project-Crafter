import subprocess
import sys
import os
import shutil
from utils.complete_readme import complete_readme

def init(project_type, project_name, show_output=True):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    file = os.path.join(script_dir, "types", project_type.replace("-", "_") + ".py")
    if not os.path.isfile(file) and project_type != "empty":
        print(f"Project type '{project_type}' does not exist.")
        return
    
    # 1. Create a new dir with the project name and go to it
    if os.path.exists(project_name):
        print(f"Directory '{project_name}' already exists.")
        return
    
    if project_type == "flutter":
        # Print text in red
        print("\033[31mI recommend u use VS Code Skeleton Project Generator\033[0m")
        os.system(f"flutter create --org com.teoneag {project_name}")
        os.chdir(project_name)
    else:
        os.makedirs(project_name)
        os.chdir(project_name)
    
    # 2. Execute the script with the project name as an argument
    if project_type != "empty":
        subprocess.run([sys.executable, file, project_name])
    
    # 3. Create gifs folder
    if not os.path.exists("gifs"):
        os.makedirs("gifs")
    
    # 4. Coppy license
    current_dir = os.getcwd()
    resources_dir = os.path.join(os.path.dirname(__file__), "..", "resources")
    shutil.copyfile(os.path.join(resources_dir, "LICENSE"), os.path.join(current_dir, "LICENSE"))
    
    # 5. Copy the README.md file
    readme_file = os.path.join(resources_dir, "README_" + project_type + ".md")
    destination_readme = os.path.join(current_dir, "README.md")
    if os.path.exists(readme_file):
        shutil.copyfile(readme_file, destination_readme)
    else:
        shutil.copyfile(os.path.join(resources_dir, "README.md"), destination_readme)
    
    # 6. Modify the readme file
    complete_readme(os.path.join(current_dir, "README.md"), project_name)
    
    if show_output:
        print(f"Project '{project_name}' initialized successfully.")