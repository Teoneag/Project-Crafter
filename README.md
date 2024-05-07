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

### fix

- asci art spansw on 2 lines with empty line

### features

- make some sort of cli (so you can change different features)
- New tool: check a project for missing/wrong stuff and add them
- add gradle that installs features (python, libraries, etc)
- add help command