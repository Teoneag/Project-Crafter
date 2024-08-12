main_path = "lib\\main.dart"


import sys
import os


oringinal_text = """You can run it directly from gradle
```bash
./gradlew run
```
Or alternatively, first build it
```bash
./gradlew build
```
And then run it
```bash
java -jar app/build/libs/app.jar
```
Or you can use IntelliJ IDEA to run it. (open the project and run the App class)
"""


replacement_text = """You can run it directly from gradle

```bash
flutter run
```

Or you can use VS Code to run it. (open the project, and on the lib/main.dart file press the run button above the main function)
"""


def init_flutter_script(project_name):

    # 1. Add to the README.md this line at the beggining "**<font color="red">ToDo delete unwanted platforms</font>**"

    readme_file = os.path.join(os.getcwd(), "README.md")

    with open(readme_file, 'r+', encoding='utf-8') as file:
        fileData = file.read()
        fileData = "**<font color=\"red\">ToDo delete unwanted platforms</font>**\n" + fileData
        fileData = fileData.replace(oringinal_text, replacement_text)

        file.seek(0)

        file.write(fileData)

        file.truncate()
    

if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Incorrect args. You need 1 arg: <project_name>")

    else:

        project_name = sys.argv[1]

        init_flutter_script(project_name)