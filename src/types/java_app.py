main_path = "app\\src\\main\\java\\com\\teoneag\\App.java"

import sys
from utils.init_java_project import init_java_project

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect args. You need 1 arg: <project_name>")
    else:
        project_name = sys.argv[1]
        init_java_project(project_name, "java-application")