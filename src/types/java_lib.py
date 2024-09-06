main_path = "lib\\src\\main\\java\\com\\teoneag\\Library.java"

import sys
import shutil
import os
from utils.init_java_project import init_java_project

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect args. You need 1 arg: <project_name>")
    else:
        # Step 1: Create a new Java Gradle app
        project_name = sys.argv[1]
        init_java_project(project_name, "java-library")