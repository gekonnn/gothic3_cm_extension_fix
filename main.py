import os

def setup_config():
    if not os.path.isfile("config.txt") or os.stat("config.txt").st_size == 0:
        # Check if config file exists, and if it doesn't create one.
        global g3_dir
        global g3_data
        global g3_datafiles
        g3_dir = str(input("Please specify Gothic 3 folder location: "))
        with open("config.txt", "a") as c:
            c.write(g3_dir)
    else:
        with open("config.txt", "r") as c:
            g3_dir = str(c.readlines()).replace('[','').replace(']','').replace("'", '')
            g3_data = g3_dir + "/Data/"
            g3_datafiles = os.listdir(g3_data)
    get_files()

def get_files():
    global compiledAnimation_files
    global compiledImage_files
    global gui_files
    global infos_files
    global projects_compiled_files
    global strings_files
    global templates_files

    compiledAnimation_files = []
    compiledImage_files = []
    gui_files = []
    infos_files = []
    projects_compiled_files = []
    strings_files = []
    templates_files = []


    for i in range(len(g3_datafiles)):
        if "_compiledAnimation" in g3_datafiles[i]:
            compiledAnimation_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "_compiledImage" in g3_datafiles[i]:
            compiledImage_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "gui" in g3_datafiles[i]:
            gui_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Infos" in g3_datafiles[i]:
            infos_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Projects_compiled" in g3_datafiles[i]:
            projects_compiled_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Strings" in g3_datafiles[i]:
            strings_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Templates" in g3_datafiles[i]:
            templates_files.append(g3_datafiles[i])

    fix_extensions()

def fix_extensions():
    for i in range(len(compiledAnimation_files)):
        os.rename(g3_data + compiledAnimation_files[i], g3_data + "_compiledAnimation.m" + f"{i:02d}")

    for i in range(len(compiledImage_files)):
        os.rename(g3_data + compiledImage_files[i], g3_data + "_compiledImage.m" + f"{i:02d}")

    for i in range(len(gui_files)):
        os.rename(g3_data + gui_files[i], g3_data + "gui.m" + f"{i:02d}")

    for i in range(len(infos_files)):
        os.rename(g3_data + infos_files[i], g3_data + "Infos.m" + f"{i:02d}")

    for i in range(len(projects_compiled_files)):
        os.rename(g3_data + projects_compiled_files[i], g3_data + "Projects_compiled.m" + f"{i:02d}")

    for i in range(len(strings_files)):
        os.rename(g3_data + strings_files[i], g3_data + "Strings.m" + f"{i:02d}")

    for i in range(len(templates_files)):
        os.rename(g3_data + templates_files[i], g3_data + "Templates.m" + f"{i:02d}")

    print("Renamed all files successfully.")
    input("Press enter to close the program.")
    exit()

setup_config()