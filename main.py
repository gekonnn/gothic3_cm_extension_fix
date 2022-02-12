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
            g3_data = g3_dir + "/Data/"
            g3_datafiles = os.listdir(g3_data)
            # Remove files other than .mXX from list so they don't get renamed.
            for i in g3_datafiles:
                if '.mod' in i:
                    g3_datafiles.remove(i)
                if '.p' in i:
                    g3_datafiles.remove(i)
                if '.c' in i:
                    g3_datafiles.remove(i)
                if '.n' in i:
                    g3_datafiles.remove(i)
            get_files()

    else:
        try:
            with open("config.txt", "r") as c:
                g3_dir = str(c.readlines()).replace('[', '').replace(']', '').replace("'", '')
                g3_data = g3_dir + "/Data/"
                g3_datafiles = os.listdir(g3_data)
                # Remove files other than .mXX from list so they don't get renamed.
                for i in g3_datafiles:
                    if '.mod' in i:
                        g3_datafiles.remove(i)
                    if '.p' in i:
                        g3_datafiles.remove(i)
                    if '.c' in i:
                        g3_datafiles.remove(i)
                    if '.n' in i:
                        g3_datafiles.remove(i)
                get_files()
        except FileNotFoundError:
            print("WARNING: Path you have specified is invalid. Please delete config.txt file and restart the program.")
            os.system("pause")
            exit()

def get_files():
    global compiledAnimation_files
    global compiledImage_files
    global compiledMaterial_files
    global compiledMesh_files
    global compiledPhysic_files
    global gui_files
    global infos_files
    global library_files
    global lightmaps_files
    global materials_files
    global music_files
    global quests_files
    global sound_files
    global speech_english_files
    global speech_polish_files
    global speech_german_files
    global projects_compiled_files
    global speedtrees_files
    global strings_files
    global templates_files
    global workspace_files

    compiledAnimation_files = []
    compiledImage_files = []
    compiledMaterial_files = []
    compiledMesh_files = []
    compiledPhysic_files = []
    gui_files = []
    infos_files = []
    library_files = []
    lightmaps_files = []
    materials_files = []
    music_files = []
    quests_files = []
    sound_files = []
    speech_english_files = []
    speech_polish_files = []
    speech_german_files = []
    speedtrees_files = []
    projects_compiled_files = []
    strings_files = []
    templates_files = []
    workspace_files = []

    print("Fetching files...")

    for i in range(len(g3_datafiles)):
        if "_compiledAnimation.m" in g3_datafiles[i]:
            compiledAnimation_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "_compiledImage.m" in g3_datafiles[i]:
            compiledImage_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "_compiledMaterial.m" in g3_datafiles[i]:
            compiledMaterial_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "_compiledMesh.m" in g3_datafiles[i]:
            compiledMesh_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "_compiledPhysic.m" in g3_datafiles[i]:
            compiledPhysic_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "gui.m" in g3_datafiles[i]:
            gui_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Infos.m" in g3_datafiles[i]:
            infos_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Library.m" in g3_datafiles[i]:
            library_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Lightmaps.m" in g3_datafiles[i]:
            lightmaps_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Materials.m" in g3_datafiles[i]:
            materials_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Music.m" in g3_datafiles[i]:
            music_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Quests.m" in g3_datafiles[i]:
            quests_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Sound.m" in g3_datafiles[i]:
            sound_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Speech_English.m" in g3_datafiles[i]:
            speech_english_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Speech_Polish.m" in g3_datafiles[i]:
            speech_polish_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Speech_German.m" in g3_datafiles[i]:
            speech_german_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Speedtrees.m" in g3_datafiles[i]:
            speedtrees_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Projects_compiled.m" in g3_datafiles[i]:
            projects_compiled_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Strings.m" in g3_datafiles[i]:
            strings_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Templates.m" in g3_datafiles[i]:
            templates_files.append(g3_datafiles[i])

    for i in range(len(g3_datafiles)):
        if "Workspace.m" in g3_datafiles[i]:
            workspace_files.append(g3_datafiles[i])

    fix_extensions()

def fix_extensions():
    print("Renaming files...")

    for i in range(len(compiledAnimation_files)):
        os.rename(g3_data + compiledAnimation_files[i], g3_data + "_compiledAnimation.m" + f"{i:02d}")

    for i in range(len(compiledImage_files)):
        os.rename(g3_data + compiledImage_files[i], g3_data + "_compiledImage.m" + f"{i:02d}")

    for i in range(len(compiledMaterial_files)):
        os.rename(g3_data + compiledMaterial_files[i], g3_data + "_compiledMaterial.m" + f"{i:02d}")

    for i in range(len(compiledMesh_files)):
        os.rename(g3_data + compiledMesh_files[i], g3_data + "_compiledMesh.m" + f"{i:02d}")

    for i in range(len(compiledPhysic_files)):
        os.rename(g3_data + compiledPhysic_files[i], g3_data + "_compiledPhysic.m" + f"{i:02d}")

    for i in range(len(gui_files)):
        os.rename(g3_data + gui_files[i], g3_data + "gui.m" + f"{i:02d}")

    for i in range(len(infos_files)):
        os.rename(g3_data + infos_files[i], g3_data + "Infos.m" + f"{i:02d}")

    for i in range(len(library_files)):
        os.rename(g3_data + library_files[i], g3_data + "Library.m" + f"{i:02d}")

    for i in range(len(lightmaps_files)):
        os.rename(g3_data + lightmaps_files[i], g3_data + "Lightmaps.m" + f"{i:02d}")

    for i in range(len(materials_files)):
        os.rename(g3_data + materials_files[i], g3_data + "Materials.m" + f"{i:02d}")

    for i in range(len(music_files)):
        os.rename(g3_data + music_files[i], g3_data + "Music.m" + f"{i:02d}")

    for i in range(len(quests_files)):
        os.rename(g3_data + quests_files[i], g3_data + "Quests.m" + f"{i:02d}")

    for i in range(len(sound_files)):
        os.rename(g3_data + sound_files[i], g3_data + "Sound.m" + f"{i:02d}")

    for i in range(len(speech_english_files)):
        os.rename(g3_data + speech_english_files[i], g3_data + "Speech_English.m" + f"{i:02d}")

    for i in range(len(speech_polish_files)):
        os.rename(g3_data + speech_polish_files[i], g3_data + "Speech_Polish.m" + f"{i:02d}")

    for i in range(len(speech_german_files)):
        os.rename(g3_data + speech_german_files[i], g3_data + "Speech_German.m" + f"{i:02d}")

    for i in range(len(speedtrees_files)):
        os.rename(g3_data + speedtrees_files[i], g3_data + "Speedtrees.m" + f"{i:02d}")

    for i in range(len(projects_compiled_files)):
        os.rename(g3_data + projects_compiled_files[i], g3_data + "Projects_compiled.m" + f"{i:02d}")

    for i in range(len(strings_files)):
        os.rename(g3_data + strings_files[i], g3_data + "Strings.m" + f"{i:02d}")

    for i in range(len(templates_files)):
        os.rename(g3_data + templates_files[i], g3_data + "Templates.m" + f"{i:02d}")

    for i in range(len(workspace_files)):
        os.rename(g3_data + workspace_files[i], g3_data + "Workspace.m" + f"{i:02d}")

    print("Renamed all files successfully.")
    os.system("pause")
    exit()

setup_config()