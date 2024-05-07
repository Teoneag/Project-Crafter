from init_java_project import init_java_project

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Incorrect args. Run: python lib.py <project_name>")
    else:
        project_name = sys.argv[1]
        init_java_project(project_name, "java-library")