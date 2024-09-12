main_path = ""

import sys

def init_flutter_script(project_name):
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect args. You need 1 arg: <project_name>")
    else:
        project_name = sys.argv[1]
        init_flutter_script(project_name)