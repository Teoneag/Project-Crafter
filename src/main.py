import sys
from init import init
from analize import analize
from rename import rename 

def help():
    print("""
Available commands:
    help
    init
    analize
    rename
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid command.")
        help()
        sys.exit(1)
    
    option = sys.argv[1]
    if option == "help":
        help()
    elif option == "init":
        if len(sys.argv) != 4:
            print("Incorrect args. Run: project init <project-type> <project-name>")
            sys.exit(1)
        init(sys.argv[2], sys.argv[3])
    elif option == "analize":
        if len(sys.argv) != 2:
            print("Incorrect args. Run: project analize")
            sys.exit(1)
        analize()
    elif option == "rename":
        if len(sys.argv) != 3:
            print("Incorrect args. Run: project rename <new-name>")
            sys.exit(1)
        rename(sys.argv[2])
    else:
        print("Invalid command.")
        help()
        sys.exit(1)