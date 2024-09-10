import sys
from init import init
from analyze import analyze
from rename import rename

commands = {
    "init": {
        "args": ["project-type", "project-name"],
        "func": lambda args: init(args[0], args[1])
    },
    "analyze": {
        "args": [],
        "func": lambda args: analyze()
    },
    "rename": {
        "args": ["new-name"],
        "func": lambda args: rename(args[0])
    }
}

def help():
    print("Available commands:")
    for cmd, info in commands.items():
        arg_list = " ".join(f"<{arg}>" for arg in info["args"])
        print(f"    {cmd} {arg_list}")
    print("    help")

if __name__ == "__main__":
    # invalid command
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Invalid command.")
        help()
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]
    expected_args = commands[command]["args"]
    
    # invalid nr of arguments
    if len(args) != len(expected_args):
        print(f"Usage: project {command} " + " ".join(f"<{arg}>" for arg in expected_args))
        sys.exit(1)
    # good command: run it
    else:
        commands[command]["func"](args)
