main_path = "app\\src\\main\\java\\com\\teoneag\\App.java"

import sys
import os
import shutil
from utils.init_java_project import init_java_project

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect args. You need 1 arg: <project_name>")
    else:
        project_name = sys.argv[1]
        init_java_project(project_name, "java-application")
        
        # Replace Main with app from readme.md
        with open(os.path.join(os.getcwd(), "README.md"), "r+", encoding="utf-8") as file:
            data = file.read()
            data = data.replace("Main", "App")
            file.seek(0)
            file.write(data)
            
        # Copy App.java from resources
        resources_dir = os.path.join(os.path.dirname(__file__), "..\\..", "resources")
        current_dir = os.getcwd()
        shutil.copyfile(os.path.join(resources_dir, "App.java"), os.path.join(current_dir, main_path))