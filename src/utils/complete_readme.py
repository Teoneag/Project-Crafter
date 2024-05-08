import pyfiglet

def ascii_art_title(project_name):
    project_name = project_name.replace('-', ' ')
    return pyfiglet.figlet_format(project_name, font = "ansi_shadow", width=110).rstrip()

def complete_readme(readme_path, project_name):
    with open(readme_path, "r+", encoding="utf-8") as file:
        formatted_content = file.read().format(ascii_art_title(project_name), project_name)
        file.seek(0)
        file.write(formatted_content)
        file.truncate()