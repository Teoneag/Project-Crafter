main_path = "lib\\main.dart"

import sys
import os

def init_flutter_script(project_name):
    # Nothing for now
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect args. You need 1 arg: <project_name>")
    else:
        project_name = sys.argv[1]
        init_flutter_script(project_name)