import subprocess
import sys
import os

def init_project(project_type, project_name):    
     # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the project type folder relative to the script's directory
    file = os.path.join(script_dir, project_type.replace("-", "\\") + ".py")
    if not os.path.isfile(file):
        print(f"Project type folder '{project_type}' does not exist.")
        return
    
    # Execute the script with the project name as an argument
    subprocess.run([sys.executable, file, project_name])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect args. Run: python init_project.py <project_type> <project_name>")
    else:
        init_project(sys.argv[1], sys.argv[2])
