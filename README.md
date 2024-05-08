<div align="center">
<pre>
██╗███╗   ██╗██╗████████╗   ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
██║████╗  ██║██║╚══██╔══╝   ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
██║██╔██╗ ██║██║   ██║█████╗██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
██║██║╚██╗██║██║   ██║╚════╝██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
██║██║ ╚████║██║   ██║      ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
</pre>
<div align="right">

Simple CLI tool to initialize a project with the basic structure.

By [Teodor Neagoe](https://github.com/Teoneag)

</div>
<img src="gifs/init-project Preview.gif" alt="init-project"/>
</div>

## Getting Started

### Prerequisites

- Os: Windows
- Gradle (for Java projects)
- python (for python projects)
  - libraries: pyfiglet

## Download

### 1. Clone the repository

```bash
git clone https://github.com/Teoneag/init-project
```

### 2. Add the path to the environment variables

1. Type in the search bar env and click on "Edit the system environment variables".
2. Click on "Environment Variables".
3. On the "System variables" section, click on "Path" and then on "Edit".
4. Click on "New" and add the path to the folder where you cloned the repository.

### 3. Run
   
```bash
init-project <project-type> <project-name>
```
Options for project-type:
- java-app
- java-lib
- python

## Plan -> Actual: 

Chronological order. Planned time -> actual time
- move the readme.md creation to main
- make it create a new folder
- make it create the gifs folder

## ToDo

- find a better name for the project: project

### Fix

- asci art spansw on 2 lines with empty line
- rename ascii art in the rename function

### Features

- make some sort of cli (so you can change different features): 10m -> 11m
  - help
  - init <type> <name>
  - analize
  - rename <oldName> <newName>
- add gradle that installs features (python, libraries, etc)
- make help better

### Tests

- test the project

### Refactor

- make the code better and easily extandable (probably switch from python to java 😢)