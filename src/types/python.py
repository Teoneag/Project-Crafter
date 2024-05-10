main_path = "src\\main.py"

import sys
import os

def init_python_script(project_name):
    # 1. Make the .gitignore file and add the test and __pycache__ folders
    with open(".gitignore", "w") as f:
        f.write("__pycache__\ntest\n")
    
    # 2. Create the src folder + main.py
    if not os.path.exists(os.path.dirname(main_path)):
        os.makedirs(os.path.dirname(main_path))
    if not os.path.exists(main_path):
        with open(os.path.join("src", "main.py"), "w") as f:
            f.write("print('Hail, Hydra...')\n")    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect args. You need 1 arg: <project_name>")
    else:
        project_name = sys.argv[1]
        init_python_script(project_name)