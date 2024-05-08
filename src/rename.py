import os
import re
from utils.complete_readme import ascii_art_title

def search_files(directory, search_strings):
    nr_appereances = 0
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    for search_string in search_strings:
                        if search_string in content:
                            print(f"Found '{search_string}' in '{file_path}' at line {content.index(search_string)}.")
                            nr_appereances += 1
            except Exception as e:
                pass
    return nr_appereances

def rename(old_name, new_name):
    
    old_name = old_name.replace("\\", "").replace(".", "")
    
    # 1. Rename dir name
    if not os.path.exists(old_name):
        print(f"Directory '{old_name}' does not exist.")
        return
    
    os.rename(old_name, new_name)
    
    os.chdir(new_name)
    current_dir = os.getcwd()
    
    # 2. Modify the readme file
    readme_file = os.path.join(current_dir,  "README.md")
    if os.path.exists(readme_file):
        with open(readme_file, 'r+', encoding='utf-8') as file:
            filedata = file.read()
            filedata = filedata.replace(old_name, new_name)
            new_ascii_art = ascii_art_title(new_name)
            filedata = re.sub(r"(?<=<pre>\n).*?(?=\n</pre>)", new_ascii_art, filedata, flags=re.DOTALL)
            file.seek(0)
            file.write(filedata)
            file.truncate()
            
    # 3. Rename gif if it exists
    gif_file = os.path.join(current_dir, "gifs", old_name + " Preview.gif")
    if os.path.exists(gif_file):
        gif_new_name = os.path.join(current_dir, "gifs", new_name + " Preview.gif")
        os.rename(gif_file, gif_new_name)
    
    # 3. For java rename settings.gradle.kts
    settings_file = os.path.join(current_dir, "settings.gradle.kts")
    if os.path.exists(settings_file):
        with open(settings_file, 'r+', encoding='utf-8') as file:
            filedata = file.read()
            filedata = filedata.replace(old_name, new_name)
            file.seek(0)
            file.write(filedata)
            file.truncate()
    
    # 4. search whole project for old project name (with spaces, with dashes, with underscores)
    old_names = [old_name, old_name.replace("-", " "), old_name.replace("-", "_")]
    nr_aparences = search_files(current_dir, old_names)
    
    print(f"The renamed project contains {nr_aparences} appearances of the old name '{old_name}'.")