import os
import sys
import time

folder_path = "C:/Users/Mus/Pictures/AllGif/"
command_list = {"list:all", "list:folder", "rename:all", "mypictures"}


def Images(command: str, usetempname: bool):
    if not command: return None

    Base_commands = command.split(":")[0]
    Argument = command.split(":")[1] if len(command.split(":")) >= 2 else None
    Folder_list = set()
    Children_list = {}
    Pictures = {}
    Number_of_files = 0

    for path, dirs, files in os.walk(folder_path):
        idx = 1
        Children_folder = False
        if len(path.split("\\")) < 2:
            Dir = path.split("/")
        else:
            Dir = path.split("\\")
            Children_folder = True
        for filename in files:
            # Base dir :
            # Exemple in : C:/Users/Mus/Pictures/AllGif/Naruto" -> Base_dir = Naruto
            # If the folder has children like : C:/Users/Mus/Pictures/AllGif/Naruto\Sasuke -> Base_dir would be again : Naruto
            Base_dir = "%s" % path.split("/")[5] if not Children_folder else path.split("/")[5].split("\\")[0]
            # If we take the exemple before, children dir would be in : C:/Users/Mus/Pictures/AllGif/Naruto\Sasuke -> Sasuke
            Children_dir = "%s" % path.split("\\")[1] if Children_folder else None
            # The extension of the file to rename with it : like .gif, .png etc
            Extension = "%s" % filename.split(".")[1]
            # Temporary name to be sure we don't rename a file with a name that already used
            temp_name = "Temp_%s.%s" % (idx, Extension)
            # New name of the file :
            # Composed with : The Base_dir name OR the children name if there are one and the extension
            # Like : Sasuke_1.gif for C:/Users/Mus/Pictures/AllGif/Naruto\Sasuke
            # And Naruto_1 gif for a file in C:/Users/Mus/Pictures/AllGif/Naruto
            new_name = "%s_%s.%s" % (Base_dir.replace(" ", "_") if not Children_folder else Children_dir.replace(" ", "_"), idx, Extension)
            # Full path is equel to the full path of the old file
            # Like : C:/Users/Mus/Pictures/AllGif/Naruto/ezgif15454.gif
            full_path = "%s/%s" % (path, filename)
            # New newnamefull is the full path of the new file name
            # Like : C:/Users/Mus/Pictures/AllGif/Naruto/Naruto_1.gif
            new_name_full = "%s/%s" % (path, new_name)
            # Temp name full
            new_temp_full = "%s/%s" % (path, temp_name)

            if Base_commands == "mypictures":
                if Pictures == {}:
                    if Children_dir is not None:
                        Pictures[Base_dir] = {}
                        Pictures[Base_dir][Children_dir] = {}
                        Pictures[Base_dir][Children_dir].update({"files": set(), "total": 0})
                        Pictures[Base_dir][Children_dir].get("files").add(new_name)
                        Pictures[Base_dir][Children_dir]["total"] = 1

                    else:
                        Pictures[Base_dir] = {}
                        Pictures[Base_dir].update({"files": set(), "total": 0})
                        Pictures[Base_dir].get("files").add(new_name)
                        Pictures[Base_dir]["total"] = 1
                
                if Pictures.get(Base_dir) is None:
                    if Children_dir is not None:
                        Pictures[Base_dir] = {}
                        Pictures[Base_dir][Children_dir] = {}
                        Pictures[Base_dir][Children_dir].update({"files": set(), "total": 0})
                        Pictures[Base_dir][Children_dir].get("files").add(new_name)
                        Pictures[Base_dir][Children_dir]["total"] = 1
                    else:
                        Pictures[Base_dir] = {}
                        Pictures[Base_dir].update({"files": set(), "total": 0})
                        Pictures[Base_dir].get("files").add(new_name)
                        Pictures[Base_dir]["total"] = 1


                if Pictures.get(Base_dir) is not None:
                    if Children_dir is not None:
                        print("Find new : %s" % Children_dir)
                        if Pictures.get(Base_dir).get(Children_dir) is not None:
                            print("again : %s" % Children_dir)
                            if new_name not in Pictures.get(Base_dir).get(Children_dir).get("files"):
                                Pictures.get(Base_dir).get(Children_dir).get("files").add(new_name)
                                Pictures.get(Base_dir).get(Children_dir)["total"] = Pictures.get(Base_dir).get(Children_dir).get("total") + 1
                        else:
                                Pictures[Base_dir][Children_dir] = {}
                                Pictures[Base_dir][Children_dir].update({"files": set(), "total": 0})
                                Pictures[Base_dir][Children_dir].get("files").add(new_name)
                                Pictures[Base_dir][Children_dir]["total"] = 1

                                
                    else:
                        if new_name not in Pictures.get(Base_dir).get("files"):
                            Pictures.get(Base_dir).get("files").add(new_name)
                            Pictures.get(Base_dir)["total"] = Pictures.get(Base_dir).get("total") + 1

                    
                    
                    

            if Base_commands == "list":
                if Argument == "all":
                    print("My pictures : [%s] " % full_path)
                    Number_of_files += 1
                if Argument == "folder":
                    if Base_dir not in Folder_list:
                        Folder_list.add(Base_dir)
                    if Children_list == {}:
                        if Children_dir is not None:
                            print("List is empty, gonna create it.")
                            print("Children list is null for %s , gonna create it with %s." % (Base_dir, Children_dir))
                            Children_list[Base_dir] = []
                            Children_list[Base_dir].append(Children_dir)
                    if Children_list.get(Base_dir) is None:
                        if Children_dir is not None:
                            print("Children list is null for %s , gonna create it with %s" % (Base_dir, Children_dir))
                            Children_list[Base_dir] = []
                            Children_list[Base_dir].append(Children_dir)
                    if Children_list.get(Base_dir) is not None:
                        if Children_dir is not None:
                            if not Children_dir in Children_list[Base_dir]:
                                print("Children list is not empty, gonna add %s for %s" % (Children_dir, Base_dir))
                                Children_list[Base_dir].append(Children_dir) 

            if Base_commands == "rename":
                if Argument == "all":
                    try:
                        if usetempname:
                            print("Renaming : [%s] in -> [%s]" % (full_path, new_temp_full))
                            os.rename(r"%s" % full_path, r"%s" % new_temp_full)
                        else:
                            print("Renaming : [%s] in -> [%s]" % (new_temp_full, new_name_full))
                            os.rename(r"%s" % new_temp_full, r"%s" % new_name_full)
                    except Exception as e:
                        print("Error occured")
                        print(e)

                    finally:
                        pass
            idx += 1
    if Base_commands == "mypictures":
        for name, dico in Pictures.items():
            if dico.get("total") is None:
                for f, t in dico.items():
                    print("Total file for [%s/%s] -> %s" % (name, f, t.get("total")))
            else:
                print("Total file for [%s] -> %s" % (name, dico.get("total")))

    if Base_commands == "list":
        if Argument == "all": 
            print("\nTotal number of files : %s" % Number_of_files)
        if Argument == "folder":
            for folder in Folder_list:
                print("Folder : %s " % folder)
                if Children_list.get(folder) is not None:
                    for child in Children_list[folder]:
                        print("[%s] -> Children : %s" % (folder, child))
            print("Total number of folder : %s " % len(Folder_list))

if not len(sys.argv) == 2:
    wanted_args = input("Enter a valid command ! (list, rename, mypictures) : ")
    while wanted_args not in command_list:
        wanted_args = input("Enter a valid command ! (list, rename, mypictures) : ")
else:
    wanted_args = sys.argv[1]


Images(wanted_args, True)
Images(wanted_args, False)


# for path, dirs, files in os.walk(folder_path):
#     idx = 1
#     Children_folder = False
#     if len(path.split("\\")) < 2:
#         Dir = path.split("/")
#     else:
#         Dir = path.split("\\")
#         Children_folder = True

#     for filename in files:
#         new_name = "%s_%s" % (Dir[5].replace(" ", "_") if not Children_folder else Dir[1].replace(" ", "_"), idx)
#         full_path = "%s/%s" % (path, filename)
#         new_name_full = "%s/%s.gif" % (path, new_name)
#         print("Renaming : [%s] in -> [%s]" % (full_path, new_name_full))
#         try:
#             os.rename(r"%s" % full_path, r"%s" % new_name_full)
#         except:
#             print("Error occured")
#         finally:
#             pass
#         idx += 1

