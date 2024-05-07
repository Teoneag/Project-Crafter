import os
import shutil
from utils.complete_readme import complete_readme

def init_python_script(project_name):
    # 1. Coppy readme, license
    current_dir = os.getcwd()
    resources_dir = os.path.join(os.path.dirname(__file__), "..", "resources")
    shutil.copyfile(os.path.join(resources_dir, "README.md"), os.path.join(current_dir, "README.md"))
    shutil.copyfile(os.path.join(resources_dir, "LICENSE"), os.path.join(current_dir, "LICENSE"))
    
    # 2. Make the .gitignore file and add the test and __pycache__ folders
    with open(".gitignore", "w") as f:
        f.write("test\n__pycache__\n")
    
    # 3. Create the src folder + main.py
    os.makedirs("src")
    with open(os.path.join("src", "main.py"), "w") as f:
        f.write("print('Hail, Hydra...')\n")
    
    # 4. Modify the readme file
    complete_readme(os.path.join(current_dir, "README.md"), project_name)
    
    print(f"Python script '{project_name}' initialized successfully.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Incorrect args. Run: python app.py <project_name>")
    else:
        project_name = sys.argv[1]
        init_python_script(project_name)