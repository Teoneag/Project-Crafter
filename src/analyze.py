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
                if main_path == "":
                    continue
                path = os.path.join(os.getcwd(), main_path)
                if os.path.exists(path):
                    return file.replace(".py", '')
    
    project_type = input("Project type not found. What's the type of the current project? It can be 'empty'\n")
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
    init(project_type, project_name, show_output=False)
    
def sync_dirs(src, dst):
    nr_changes = 0
    nr_fixed_changes = 0
    
    # Walk through the source directory
    for dirpath, dirnames, filenames in os.walk(src):
        # Calculate relative path to use in destination
        rel_path = os.path.relpath(dirpath, src)
        dst_path = os.path.join(dst, rel_path)

        # Ensure corresponding directory exists in destination
        if not os.path.exists(dst_path):
            nr_changes += 1
            answer = input(f"Do you want to add this missing dir? (y/n)\n{dst_path}\n")
            if answer.lower() != 'y':
                print(f"Skipping {dst_path}...")
                continue
            nr_fixed_changes += 1
            os.makedirs(dst_path)
            print(f"Directory {dst_path} added.")

        # Copy each file in the current directory to the destination directory
        
        for file in filenames:
            src_file = os.path.join(dirpath, file)
            dst_file = os.path.join(dst_path, file)
            if not os.path.exists(dst_file):
                nr_changes += 1
                answer = input(f"Do you want to add this missing file? (y/n)\n{dst_file}\n")
                if answer.lower() != 'y':
                    print(f"Skipping {dst_file}...")
                    continue
                nr_fixed_changes += 1
                shutil.copy2(src_file, dst_file)
                print(f"File {dst_file} added.")
                
    return nr_changes, nr_fixed_changes          

def analyze():
    current_dir = os.getcwd()
    helper_dir = os.path.join(current_dir, "project_help")
    project_name = os.path.basename(current_dir)
    
    project_type = _get_project_type()
    
    _init_helper_dir(project_type, helper_dir, project_name)
    
    project_helper_dir = os.path.join(helper_dir, project_name)
    nr_changes, nr_fixed_changes = sync_dirs(project_helper_dir, current_dir)

    os.chdir(current_dir)
    shutil.rmtree(helper_dir)
    
    if nr_changes == 0:
        print("No changes detected.")
    else:
        print(f"\nFixed {nr_fixed_changes} out of {nr_changes} changes.")