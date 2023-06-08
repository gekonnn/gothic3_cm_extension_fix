import configparser
import locale
import ctypes
import ast
import sys
import os
import re

config = configparser.ConfigParser()

# Get system language
windll = ctypes.windll.kernel32
locale_id = windll.GetUserDefaultUILanguage()
user_lang = locale.windows_locale[ locale_id ]
default_lang = "en_US"

# Read config file
try:
    config.read('config.ini')
    config_lang     = config.get('G3CMEF', 'language')
    config_dir      = config.get('G3CMEF', 'gothicdir')
    config_debug    = config.getboolean('DEBUG',  'debug')
    if not os.path.exists(config_dir):
        config_dir = "auto"
# Set default values if it doesn't exist
except:
    config_lang     = "auto"
    config_dir      = "auto"
    config_debug    = False

data_files =    ["_compiledAnimation", "_compiledImage", "_compiledMaterial", "_compiledMesh", "_compiledPhysic", 
                "gui", "Infos", "Library", "Lightmaps", "Materials", "Music", "Quests", "Sound", "Strings",
                "Speech_English", "Speech_Polish", "Speech_German", "Speech_Russian", "Projects_compiled",
                "Templates", "Workspace"]
common_dirs =   ["C:\Program Files (x86)\Steam\steamapps\common\Gothic 3",
                "C:\Program Files (x86)\GOG Galaxy\Games\Gothic 3"
                "C:\Program Files (x86)\Gothic III",
                "C:\Games\Gothic 3"
                "D:\Steam\steamapps\common\Gothic 3"
                "D:\Gothic 3"]

extensions = {}
ext_pattern = re.compile(r"^.m[0-9][0-9]")

# Set program language
if config_lang == "auto":
    if os.path.exists(f'locale/{user_lang}.txt'):
        with open(f"locale/{user_lang}.txt", encoding="utf-8") as a:
            locale_file = ast.literal_eval(a.read())
    else:
        try:
            with open(f"locale/{default_lang}.txt", encoding="utf-8") as a:
                locale_file = ast.literal_eval(a.read())
        except:
                print('[!] Language files not found!')
                input("Press ENTER to exit.")
                sys.exit()
else:
    with open(f"locale/{config_lang}.txt", encoding="utf-8") as a:
        locale_file = ast.literal_eval(a.read())


# Try automatically searching for G3 directory, using directories from list above
def dir_search():
    if config_dir == "auto":
        for dir in common_dirs:
            debuglog(f"Checking for Gothic directory in: {dir}")
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
    else:
        gothic_path = config_dir
        sort_files(gothic_path)


def specify_path():
    gothic_path = input(lang('specify_path')) + "\Data"
    if not os.path.exists(gothic_path):
        print(lang('invalid_path'))
        specify_path()
    else:
        sort_files(gothic_path)


def sort_files(gothic_path):
    anomalies = 0
    clear()
    
    if config_dir != "auto":
        print(lang('analyzing').format(config_dir))
    
    for f in os.listdir(gothic_path):
        debuglog(f'Analyzing {f}...')
        file = os.path.splitext(f)
        file_name = file[0]
        file_extension = file[1]
        if file_name in data_files:
            if re.match(ext_pattern, file_extension):
                debuglog(f'{f} is a .mxx format, analyzing...')
                extension_number = int(file_extension[2:])
                if extension_number == extensions.get(file_name, 0):
                    debuglog(f'{f} is correctly sorted.')
                    extensions[file_name] = extension_number + 1
                else:
                    for new_extension in range(extensions.get(file_name, 0), 100):
                        new_filename = f"{file_name}" + ".m{:02d}".format(new_extension)
                        if not os.path.exists(os.path.join(gothic_path, new_filename)):
                            print(lang('anomaly_found').format(f))
                            debuglog(f'{f} is not sorted.')
                            os.rename(os.path.join(gothic_path, f), os.path.join(gothic_path, new_filename))
                            debuglog(f'{f} -> {new_filename}')
                            extensions[file_name] = new_extension + 1
                            anomalies =+ 1
                            break
            else:
                debuglog(f'{f} - Not an .mxx format, skipping...')

    if anomalies == 0:
        print(lang('no_anomalies'))
    else:
        print(lang('rename_success'))
    wait_for_exit()


def wait_for_exit():
    input(lang('wait_for_exit'))
    sys.exit()


def lang(key):
    return locale_file.get(key)


def clear():
    if not config_debug:
        os.system('cls' if os.name=='nt' else 'clear')


def debuglog(string):
    if config_debug:
        print(f"[DEBUG] {string}")


clear()
dir_search()