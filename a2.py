
# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Emily Liang
# exliang@uci.edu
# 79453973

from pathlib import Path, PurePath


def main():
    user_input()


def user_input():
    while True:
        user_command = input()  # format: [COMMAND] [INPUT] [[-]OPTION] [INPUT]
        command_list = user_command.split()
        command = command_list[0]

        if command == 'Q':
            quit()
        elif len(command_list) == 1:  # user only inputs a letter & no dir
            print("ERROR")
        else:
            path = command_list[1]
            myPath = Path(path)

            # ensuring proper whitespace handling
            path = [command_list[1]]  # part of path
            for part in command_list[2:]:
                if part.startswith("-"):  # reached next command (ex: -r)
                    break
                elif ("\\" in part) or ("/" in part) or ("." in part):
                    path.append(part)  # part of path (file or dir)
            myPath = " ".join(path)
            for part in command_list[:]:  # copy of lst bc of indexing
                if part.startswith("-"):  # reached next command (ex: -r)
                    break
                elif ("\\" in part) or ("/" in part) or ("." in part):
                    command_list.remove(part)  # remove old path in command_lst
            command_list.insert(1, myPath)  # insert new path into list
            myPath = Path(myPath)  # new path

            if myPath.exists():  # ensure that directory exists
                if command == 'L':  # list contents of directory
                    if len(command_list) == 2:  # [COMMAND] [INPUT]
                        if "." in str(myPath):  # last part is a file
                            print("ERROR")
                        else:
                            list_directories(myPath)
                    elif len(command_list) == 3:  # [C] [INPUT] [[-]OPTION]
                        option = command_list[2]
                        if option == '-r':
                            recursive(myPath)
                        elif option == '-f':  # output files only
                            list_files(myPath)
                        else:  # invalid command
                            print("ERROR")
                    elif len(command_list) == 4:  # [C][I][[-]O][I]
                        option = command_list[2]
                        if option == '-s':  # output files that match file name
                            file_name = command_list[3]
                            if "." not in file_name:  # ensure file is entered
                                print("ERROR")
                            else:
                                matching_files(myPath, file_name)
                        elif option == '-e':
                            file_extension = command_list[3]
                            if len(file_extension) != 3:
                                print("ERROR")
                            else:
                                matching_extension(myPath, file_extension)
                        elif option == '-r':  # -r -f
                            option2 = command_list[3]
                            recursive_f(myPath)
                        else:  # invalid command
                            print("ERROR")
                    elif len(command_list) == 5:  # [C][I][[-]O][I][I]
                        option = command_list[2]
                        option2 = command_list[3]
                        if option == '-r' and option2 == '-s':  # -r -s filen.e
                            file_name = command_list[4]
                            if "." not in file_name:  # ensure file is entered
                                print("ERROR")
                            else:
                                recursive_s(myPath, file_name)
                        elif option == '-r' and option2 == '-e':  # -r -e filee
                            file_extension = command_list[4]
                            if file_extension.isnumeric():  # fileex has nums
                                print("ERROR")
                            else:
                                recursive_e(myPath, file_extension)
                        else:  # invalid command
                            print("ERROR")
                elif command == "C":  # create new DSU file
                    filename = command_list[3]
                    if command_list[2] != "-n":
                        print("ERROR")
                    else:
                        command_C(myPath, filename)
                elif command == "D":  # delete DSU file
                    command_D(myPath)
                elif command == "R":  # read file contents
                    command_R(myPath)
                else:  # invalid command
                    print("ERROR")
                    get_path()
            else:
                if command == "D" or command == "R":
                    command_D(myPath)
                else:
                    print("Directory doesn't exist. Try again.")


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
    print(myPath.joinpath(filename + ".dsu"))
    username = input("Enter a unique name: ")
    password = input("Enter a password: ")
    bio = input("Enter a brief description of the user: ")


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


if __name__ == '__main__':
    main()

# Citations:
# - https://docs.python.org/3/library/pathlib.html 
