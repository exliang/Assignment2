
# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Emily Liang
# exliang@uci.edu
# 79453973

from pathlib import Path, PurePath
import Profile
import ui

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
                            ui.list_directories(myPath)
                    elif len(command_list) == 3:  # [C] [INPUT] [[-]OPTION]
                        option = command_list[2]
                        if option == '-r':
                            ui.recursive(myPath)
                        elif option == '-f':  # output files only
                            ui.list_files(myPath)
                        else:  # invalid command
                            print("ERROR")
                    elif len(command_list) == 4:  # [C][I][[-]O][I]
                        option = command_list[2]
                        if option == '-s':  # output files that match file name
                            file_name = command_list[3]
                            if "." not in file_name:  # ensure file is entered
                                print("ERROR")
                            else:
                                ui.matching_files(myPath, file_name)
                        elif option == '-e':
                            file_extension = command_list[3]
                            if len(file_extension) != 3:
                                print("ERROR")
                            else:
                                ui.matching_extension(myPath, file_extension)
                        elif option == '-r':  # -r -f
                            option2 = command_list[3]
                            ui.recursive_f(myPath)
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
                                ui.recursive_s(myPath, file_name)
                        elif option == '-r' and option2 == '-e':  # -r -e filee
                            file_extension = command_list[4]
                            if file_extension.isnumeric():  # fileex has nums
                                print("ERROR")
                            else:
                                ui.recursive_e(myPath, file_extension)
                        else:  # invalid command
                            print("ERROR")
                elif command == "C":  # create new DSU file
                    filename = command_list[3]
                    if command_list[2] != "-n":
                        print("ERROR")
                    else:
                        ui.command_C(myPath, filename)
                elif command == "D":  # delete DSU file
                    ui.command_D(myPath)
                elif command == "R":  # read file contents
                    ui.command_R(myPath)
                else:  # invalid command
                    print("ERROR")
                    ui.get_path()
            else:
                if command == "D" or command == "R":
                    ui.command_D(myPath)
                else:
                    print("Directory doesn't exist. Try again.")


if __name__ == '__main__':
    main()

# Citations:
# - https://docs.python.org/3/library/pathlib.html
