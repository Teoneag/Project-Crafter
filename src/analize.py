import os
import sys
import shutil
from init import init

def _get_project_type():
    types_dir = os.path.join(os.path.dirname(__file__), "types")
    
    for file in os.listdir(types_dir):
        full_path = os.path.join(types_dir, file)
        if os.path.isfile(full_path):
            with open(full_path, "r") as f:
                main_path = f.readline().replace('main_path = "', "").replace('"', "").replace("\\\\", "\\").strip()
                path = os.path.join(os.getcwd(), main_path)
                if os.path.exists(path):
                    return file.replace('.py', '')
    
    project_type = input("Project type not found. What's the type of the current project?\n")
    if not os.path.isfile(os.path.join(types_dir, project_type + ".py")):
        print("Project type not found. Type project help to see the available project types.")
        sys.exit(1)
    return project_type

def _init_helper_dir(project_type, helper_dir, project_name):
    if os.path.exists(helper_dir):
        answer = input("The directory 'project_help' already exists. Do you want to overwrite it? (y/n)\n")
        if answer.lower() != 'y':
            print("Aborting...")
            sys.exit(1)
        shutil.rmtree(helper_dir)
    os.makedirs(helper_dir)
    os.chdir(helper_dir)
    init(project_type, project_name)

def analize():
    current_dir = os.getcwd()
    helper_dir = os.path.join(current_dir, "project_help")
    project_name = os.path.basename(current_dir)
    
    project_type = _get_project_type()
    
    _init_helper_dir(project_type, helper_dir, project_name)
    
    # compare files in the helper dir with the current project, and print the missing files
    project_helper_dir = os.path.join(helper_dir, project_name)
    helper_files = set()
    for root, dirs, files in os.walk(project_helper_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), project_helper_dir)
            helper_files.add(rel_path)
    current_files = set()
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), current_dir)
            current_files.add(rel_path)
    
    missing_files = helper_files - set(current_files)
    if missing_files == set():
        print("No missing files.")
    else:
        print(f"Missing files: {missing_files}")       
        answer = input("Do you want to add all those missing files? (y/n)\n")
        if answer.lower() == 'y':
            for file in missing_files:
                dir = os.path.dirname(file)
                if dir:
                    os.makedirs(os.path.join(current_dir, dir), exist_ok=True)
                shutil.copyfile(os.path.join(project_helper_dir, file), os.path.join(current_dir, file))
            print("Files added successfully.")

    # remove the helper dir
    os.chdir(current_dir)
    shutil.rmtree(helper_dir)