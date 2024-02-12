
# a2.py

# Starter code for assignment 2 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Emily Liang
# exliang@uci.edu
# 79453973

from pathlib import Path
import Profile
import ui
from shlex import split


def main():
    print("Welcome!")
    # pass in admin as False to run the interface
    user_input(printing_user_interface(False))


def user_input(user_command):
    is_admin = False
    while True:
        if user_command == "admin":  # user command is admin
            is_admin = True
            user_command = input()
        else:  # user_command is not admin
            if is_admin:  # if admin mode was already called
                user_command = input()

        if user_command[0] == 'P' or user_command[0] == 'E':
            command_list = split(user_command)
        else:
            command_list = user_command.split()
        command = command_list[0]

        if command == 'Q':
            quit()
        elif len(command_list) == 1 and command != "admin":
            print("ERROR")  # user only inputs a letter & no dir
        elif command == "admin":
            is_admin = True
            user_command = input()
        else:
            path = command_list[1]
            myPath = Path(path)

            if command != 'P' and command != 'E':  # dont check for E & P
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
                        command_list.remove(part)  # remove old path
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
                    if command_list[2] != "-n":
                        print("ERROR")
                    else:
                        filename = command_list[3]
                        my_profile, newPath = ui.command_C(myPath, filename)
                elif command == "D":  # delete DSU file
                    ui.command_D(myPath)
                elif command == "R":  # read file contents
                    ui.command_R(myPath)
                elif command == "O":  # open exisiting dsu file
                    my_profile, newPath = ui.command_O(myPath)
                else:  # invalid command
                    print("ERROR")
                    ui.get_path(dsufile)
            else:
                if command == "D" or command == "R":
                    ui.command_D(myPath)
                elif command == "E":  # edit dsu file
                    ui.command_E(newPath, command_list, my_profile)
                elif command == "P":  # printing data from dsu file
                    ui.command_P(myPath, command_list, my_profile)
                else:
                    print("Directory doesn't exist. Try again.")
        if not is_admin:  # after executing command & not admin
            # print interface & get next command
            user_command = printing_user_interface(is_admin)


def printing_user_interface(is_admin):  # Menu of options
    if not is_admin:
        print("\nHere are the possible command options:\n")
        print(" L - list contents of directory (has sub-commands) ~ FORMAT: 'L path'")
        print("   -r -> ouput directory content recursively ~ FORMAT: 'L path -r'")
        print("   -f -> output files only                   ~ FORMAT: 'L path -f'")
        print("   -s -> output files given a file name      ~ FORMAT: 'L path -s filename.extension'")
        print("   -e -> output files given a file extension ~ FORMAT: 'L path -e fileextension'")
        print("    Other valid ~ FORMATS: 'L path -r -f', 'L path -r -s filename.extension', 'L path -r -e fileextension'\n")
        print(" C - create a new journal & acquire username, password, & bio ~ FORMAT: 'C path -n filename'\n")
        print(" D - delete a dsu file ~ FORMAT: 'D path_to_dsu_file'\n")
        print(" R - read contents of a dsu file ~ FORMAT: 'R path_to_dsu_file'\n")
        print(" O - open a journal ~ FORMAT: 'O path_to_dsu_file'\n")
        print(" E - edit a journal (has sub-commands) ~ FORMAT: 'E subcommand text'")
        print("   NOTE: must call C or O command before calling E command!")
        print("   -usr     -> edits username of the journal  ~ FORMAT: 'E -usr username'")
        print("   -pwd     -> edits password of the journal  ~ FORMAT: 'E -pwd password'")
        print("   -bio     -> edits biography of the journal ~ FORMAT: 'E -bio biography'")
        print("   -addpost -> adds a post to the journal     ~ FORMAT: 'E -addpost newpost'")
        print("   -delpost -> deletes a post in the journal  ~ FORMAT: 'E -delpost postnumber' (postnumber starts at 0)")
        print("    NOTE: can type in any combination of the options above!\n")
        print(" P - output data stored in journal ~ FORMAT: P command optionaltext")
        print("   NOTE: must call C or O command before calling P command!")
        print("   -usr   -> outputs username stored in the journal  ~ FORMAT: 'P -usr'")
        print("   -pwd   -> ouputs password stored in the journal   ~ FORMAT: 'P -pwd'")
        print("   -bio   -> outputs biography stored in the journal ~ FORMAT: 'P -bio'")
        print("   -posts -> outputs all posts stored in the journal ~ FORMAT: 'P -posts'")
        print("   -post  -> outputs a post by its postnumber        ~ FORMAT: 'P -post postnumber' (postnumber starts at 0)")
        print("   -all   -> outputs all content in the journal      ~ FORMAT: 'P -all'")
        print("    NOTE: can type in any combination of the options above!\n")
        print(" Q - quit the program ~ FORMAT: 'Q' \n")
        print(" Admin mode - disables user friendly interface ~ FORMAT: 'admin'\n")
        user_command = input("Type the format you would like: ")
        return user_command


if __name__ == '__main__':
    main()

# Citations:
# - https://docs.python.org/3/library/pathlib.html
# - https://docs.python.org/3/library/shlex.html#module-shlex
