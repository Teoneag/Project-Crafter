<div align="center">
<pre>
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
                                                          
 ██████╗██████╗  █████╗ ███████╗████████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║     ██████╔╝███████║█████╗     ██║   █████╗  ██████╔╝
██║     ██╔══██╗██╔══██║██╔══╝     ██║   ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║██║        ██║   ███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝
</pre>
<div align="right">
Simple CLI tool to "craf" projects from templates: initialize, analyze, rename.

For now it only supports Python, Java applications and Java libraries.

By [Teodor Neagoe](https://github.com/Teoneag)
</div>
</div>

## Functions Preview

| Init | Analyze | Rename |
|------|---------|--------|
| <img src="gifs/Project-Crafter Preview init.gif" alt="Project-Crafter init"/> | <img src="gifs/Project-Crafter Preview analyze.gif" alt="Project-Crafter analyze"/> | <img src="gifs/Project-Crafter Preview rename.gif" alt="Project-Crafter rename"/> |


## Getting Started

### Prerequisites

- Os: Windows
- Gradle (for Java projects)
- Python (for Python projects)
  - it automatically installs pigfile library

## Download

### 1. Clone the repository

```bash
git clone https://github.com/Teoneag/Project-Crafter
```

### 2. Add the path to the environment variables

1. Type in the search bar env and click on "Edit the system environment variables".
2. Click on "Environment Variables".
3. On the "System variables" section, click on "Path" and then on "Edit".
4. Click on "New" and add the path to the folder where you cloned the repository.

## 3. Ussage

### Init

```bash
proj init <project-type> <project-name>
```
Options for project-type:
- flutter
- java-app
- java-lib
- java-swing
- python

### Analyze

```bash
proj analyze
```

### Rename

```bash
proj rename <old-name> <new-name>
```

If you don't like the "executable name" (proj), just rename the proj.bat to whatever you want.

## Plan -> Actual: 

Chronological order. Planned time -> actual time
- move the readme.md creation to main
- make it create a new folder
- make it create the gifs folder
- make some sort of cli (so you can change different features): 10m -> 11m
  - help
  - init <type> <name>
  - analize
  - rename <oldName> <newName>
- asci art spansw on 2 lines with empty line
- rename ascii art in the rename function
- find a better name for the project: projectCrafter
- call it from terminal with both projectCrafter and proj
- record new gif
- modify the java-lib README.md
- fix java-lib project creation doesn't work: 10m -> 6:34 -> 7:48
- automatically install pigfile library: 10m -> 13m
- fix proj spaces for ascii art: 5m

## ToDo

- automatically install gradle if it's not installed
  
- make the readme be made out of the different sections, so it's easier to edit for each of them
  - for example, for java add Java: 22 to the prerequisites
- for Intellij, deselect analyze code from the settings for the git

### Fix

- this random bug
```bash
D:\apps>project rename init-project Project-Crafter
Found 'init-project' in 'D:\apps\Project-Crafter\.git\config' at line 182.
Found 'init-project' in 'D:\apps\Project-Crafter\.git\FETCH_HEAD' at line 86.
The renamed project contains 2 appearances of the old name 'init-project'.
The system cannot find the path specified.

D:\apps>cd Project-Crafter
```
### Features

- make help better

### Tests

- test the project

### Refactor

- make the code better and easily extandable (probably switch from python to java 😢)