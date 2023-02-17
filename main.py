import locale
import ctypes
import ast
import os

windll = ctypes.windll.kernel32
locale_id = windll.GetUserDefaultUILanguage()

data_files = ["_compiledAnimation", "_compiledImage", "_compiledMaterial", "_compiledMesh", "_compiledPhysic", 
                "gui", "Infos", "Library", "Lightmaps", "Materials", "Music", "Quests", "Sound", "Strings",
                "Speech_English", "Speech_Polish", "Speech_German", "Speech_Russian", "Projects_compiled",
                "Templates", "Workspace"]
extensions = {}
ext_pattern = ".m{:02d}"

# Get system language
if locale_id == 1033 or 1031 or 1045:
    global user_lang
    if locale_id == 1033:
        user_lang = "en_US"
    if locale_id == 1031:
        user_lang = "de_DE"
    if locale_id == 1045:
        user_lang = "pl_PL"
else:
    user_lang = "en_US"



def wait_for_exit():
    input(lang('wait_for_exit'))
    exit()

def lang(key):
    return locale_file.get(key)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()

# Check if language files exist
if not os.path.exists("locale/en_US.txt"):
    print('[!] Language files not found!')
    input("Press ENTER to exit.")
    exit()
else:
    # Set program language
    with open("locale/%s.txt" % user_lang, encoding="utf-8") as a:
        locale_file = ast.literal_eval(a.read())

autocheck_dirs =   ["C:\Program Files (x86)\Steam\steamapps\common\Gothic 3",
                    "C:\Program Files (x86)\GOG Galaxy\Games\Gothic 3"
                    "C:\Program Files (x86)\Gothic III",
                    "D:\Steam\steamapps\common\Gothic 3"
                    "D:\Gothic 3"]

# Try automatically searching for G3 directory, using directories from list above
def dir_search():
    for dir in autocheck_dirs:
        if os.path.exists(dir):
            if "Gothic3.exe" in os.listdir(dir):
                found = True
                confirm = input(lang('path_found').format(dir)).strip().upper()
                if confirm == "Y":
                    gothic_path = f"{dir}\Data"
                    sort_files(gothic_path)
                elif confirm == "N":
                    specify_path()
    if not found:
        specify_path()

def specify_path():
    gothic_path = input(lang('specify_path')) + "\Data"
    if not os.path.exists(gothic_path):
        print(lang('invalid_path'))
        specify_path()
    else:
        sort_files(gothic_path)

def sort_files(gothic_path):
    clear()
    
    anomalies = 0
    
    for f in os.listdir(gothic_path):
        file = os.path.splitext(f)
        file_name = file[0]
        file_extension = file[1]
        if file_name in data_files:
            if file_extension.startswith(".m") and file_extension != ".mod":
                extension_number = int(file_extension[2:])
                if extension_number == extensions.get(file_name, 0):
                    extensions[file_name] = extension_number + 1
                else:
                    for new_extension in range(extensions.get(file_name, 0), 100):
                        new_filename = f"{file_name}{ext_pattern.format(new_extension)}"
                        if not os.path.exists(os.path.join(gothic_path, new_filename)):
                            print(lang('anomaly_found').format(f))
                            os.rename(os.path.join(gothic_path, f), os.path.join(gothic_path, new_filename))
                            extensions[file_name] = new_extension + 1
                            anomalies =+ 1
                            break
    
    if anomalies == 0:
        print(lang('no_anomalies'))
    else:
        print(lang('rename_success'))

    wait_for_exit()

dir_search()
