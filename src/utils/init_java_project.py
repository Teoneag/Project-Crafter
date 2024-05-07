import subprocess
import os
import shutil
from utils.complete_readme import complete_readme

def init_java_project(project_name, project_type):
    try:
        # Step 1: Create a new Java Gradle app by running
        os.system(f"gradle init --type {project_type} --package com.teoneag --project-name {project_name} --no-comments --use-defaults")
        
        # Step 2: delete .gitalttributes file
        if os.path.exists(".gitattributes"):
            os.remove(".gitattributes")
        
        # Step 3: Modify .gitignore: add idea
        with open(".gitignore", "r+") as f:
            if "idea" not in f.read():
                f.seek(0, os.SEEK_END)
                f.write("\nidea")
            
        # Step 4: Coppy checkstyle.xml, readme and license files from java/resources
        current_dir = os.getcwd()
        resources_dir = os.path.join(os.path.dirname(__file__), "..", "..", "resources")
        shutil.copyfile(os.path.join(resources_dir, "checkstyle.xml"), os.path.join(current_dir, "checkstyle.xml"))
        shutil.copyfile(os.path.join(resources_dir, "README.md"), os.path.join(current_dir, "README.md"))
        shutil.copyfile(os.path.join(resources_dir, "LICENSE"), os.path.join(current_dir, "LICENSE"))
        
        # Step 5: Add project name to readme
        complete_readme(os.path.join(current_dir, "README.md"), project_name)
        
        print(f"Java app '{project_name}' initialized successfully.")
    except Exception as e:
        print(f"Error: {e}")