main_path = "app\\src\\main\\java\\com\\teoneag\\App.java"

import sys
import os
import shutil
from utils.init_java_project import init_java_project

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect args. You need 1 arg: <project_name>")
    else:
        # Step 1: Create a new Java Gradle app
        project_name = sys.argv[1]
        init_java_project(project_name, "java-application")
        
        # Step 3: add main manifest attribute in build.gradle.kts
        with open("app\\build.gradle.kts", "r+") as f:
            content = f.read()
            f.seek(0, os.SEEK_END)
            f.write("""

    tasks.withType<Jar> {
        manifest {
            attributes["Main-Class"] = "com.teoneag.App"
        }
    }
    """)