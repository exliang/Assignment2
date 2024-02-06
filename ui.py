
# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Emily Liang
# exliang@uci.edu
# 79453973

from pathlib import Path, PurePath
import Profile

def list_directories(myPath):
    if any(myPath.iterdir()):  # check if directory isnt empty
        dir_list = []
        file_list = []
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file():  # if is file, put it in the file list
                file_list.append(currentPath)
            elif currentPath.is_dir():  # if it's a dir, put in the dir list
                dir_list.append(currentPath)
        file_list.extend(dir_list)  # combine lists (files first)
        combined_list = file_list
        for directory in combined_list:
            print(directory)


def list_files(myPath):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file():  # list files only
                print(currentPath)


def matching_files(myPath, file_name):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file() and currentPath.name == file_name:
                print(currentPath)


def matching_extension(myPath, file_extension):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.name.endswith(file_extension):  # file type = file e
                print(currentPath)


def recursive(myPath):
    dir_list = []
    if not any(myPath.iterdir()):  # if there's no more folders in directory
        return
    elif any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file():  # if it's a file, print it
                print(currentPath)
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_dir():  # if a dir, call func recursively
                dir_list.append(currentPath)
                print(currentPath)
                recursive(currentPath)


def recursive_f(myPath):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if not currentPath.is_dir():
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():  # if a dir, call func recursively
                recursive_f(currentPath)


def recursive_s(myPath, file_name):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.is_file() and currentPath.name == file_name:
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():  # if a dir, call func recursively
                recursive_s(currentPath, file_name)


def recursive_e(myPath, file_extension):
    if any(myPath.iterdir()):  # check if directory isnt empty
        for currentPath in myPath.iterdir():  # list contents of the directory
            if currentPath.name.endswith(file_extension):  # file type = file e
                print(currentPath)
        for currentPath in myPath.iterdir():
            if currentPath.is_dir():  # if a dir, call func recursively
                recursive_e(currentPath, file_extension)


def command_C(myPath, filename):
    newfile = open(filename + ".dsu", "a")
    myPath = myPath.joinpath(filename + ".dsu")
    # print(myPath)
    username = input("Enter a unique name: ")
    password = input("Enter a password: ")
    bio = input("Enter a brief description of the user: ")
    profile = Profile.Profile(None, username, password)  # creating obj Profile
    profile.bio = bio  # setting the bio
    profile.save_profile(myPath)  # saving data
    print("Data saved.")


def command_D(myPath):
    while True:
        dsufile = get_path_parts(myPath)
        if not dsufile.endswith(".dsu"):  # if file isn't DSU file
            print("ERROR")
            myPath = get_path(dsufile)  # so that myPath changes
        else:  # file is DSU file
            Path.unlink(dsufile)  # delete file from path
            print(myPath, "DELETED")  # output the path
            break


def command_R(myPath):
    while True:
        dsufile = get_path_parts(myPath)
        if not dsufile.endswith(".dsu"):  # if file isn't DSU file
            print("ERROR")
            myPath = get_path(dsufile)
        elif myPath.stat().st_size == 0:  # file_size = myPath.stat().st_size
            print("EMPTY")
            myPath = get_path(dsufile)
        else:  # print file contents
            print(myPath.read_text().strip())
            break


def command_O(myPath):
    while True:
        dsufile = get_path_parts(myPath)
        if not dsufile.endswith(".dsu"):  # if file isn't DSU file
            print("ERROR")
            myPath = get_path(dsufile)
        else:
        	f = open(dsufile)
        	print(dsufile, "opened!")
        	break


def get_path(dsufile):
    user_command = input()  # keep on asking for input
    command_list = user_command.split()
    myPath = Path(command_list[1])
    return myPath


def get_path_parts(myPath):
    p = PurePath(myPath)
    dir_tuple = p.parts[1:]  # getting parts of dir (ignoring C:\)
    dsufile = dir_tuple[len(dir_tuple)-1]
    return dsufile
