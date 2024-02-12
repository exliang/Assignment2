# ui.py

# Starter code for assignment 2 in ICS 32
# Programming with Software Libraries in Python

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
    while True:
        username = input("Enter a unique name: ")
        password = input("Enter a password: ")
        bio = input("Enter a brief description of the user: ")

        newPath = myPath.joinpath(filename + ".dsu")
        if newPath.is_file() and newPath.exists():  # file already exists
            file = open(filename + ".dsu", "a")  # load file
        else:  # create file only after data is collected
            newfile = open(filename + ".dsu", "a")

        # ensuring empty strings or whitespace strings are not added
        profile = Profile.Profile()  # creating obj Profile
        profile.bio = bio
        if not whitespace_checker(username):
            profile.username = username
        if not whitespace_checker(password):
            profile.password = password
        if not whitespace_checker(username) and not whitespace_checker(password):
            profile.save_profile(newPath)  # saving data
            print("Data saved.")
            break
        else:
            print("Invalid username and password.")
    return profile, newPath


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
        # check if dsu file follows Profile format
        profile_O = Profile.Profile()
        try:
            profile_O.load_profile(myPath)
        except:
            print("DSU file doesn't follow the Profile format.")
            break
        if not dsufile.endswith(".dsu"):  # if file isn't DSU file
            print("ERROR")
            myPath = get_path(dsufile)
        else:
            f = open(dsufile)
            print(dsufile, "opened!")
            break
    return profile_O, myPath


def command_E(myPath, command_list, profile):

    dictionary = user_input_dict(command_list)

    for command, text in dictionary.items():
        # ensuring whitespace or empty strings aren't added
        if isinstance(text, int) or not check_if_only_space(text):
            if command == "-usr":  # add username to dsu file
                if whitespace_checker(text):  # username contains whitespace
                    print("Error: Username will not be added as there is whitespace.")
                    break  # breaking out of loop so options after are not run
                else:
                    profile.username = text
            elif command == "-pwd":  # add password to dsu file
                if whitespace_checker(text):
                    print("Error: Password will not be added as there is whitespace.")
                    break  # breaking out of loop so options after are not run
                else:
                    profile.password = text
            elif command == "-bio":  # add bio to dsu file
                profile.bio = text
            elif command == "-addpost":  # add post to dsu file
                post = Profile.Post()  # create post obj w entry & timestamp
                post.entry = text
                post.timestamp = post.timestamp
                profile.add_post(post)
            elif command == "-delpost":  # delete post from dsu file
                profile.del_post(text)  # text = index
            profile.save_profile(myPath)
        else:  # text is all whitespace or is an empty string
            print("Invalid input.")
            break


def command_P(myPath, command_list, profile):
    while True:
        dictionary = user_input_dict(command_list)  # {"-pwd": "", "-post": #}
        for command, text in dictionary.items():
            if command == "-usr":
                print(f'Username: {profile.username}')
            elif command == "-pwd":
                print(f'Password: {profile.password}')
            elif command == "-bio":
                print(f'Bio: {profile.bio}')
            elif command == "-posts":
                print(f'All posts: {profile.get_posts()}')
            elif command == "-post":
                post_list = profile.get_posts()
                for i in range(len(post_list)):
                    if i == text:  # index matches
                        print(f'Post at index {i}: {post_list[i]}')
            elif command == "-all":
                print(f'Username: {profile.username}\nPassword: {profile.password}\nBio: {profile.bio}\nAll posts: {profile.get_posts()}')
        break


def user_input_dict(command_list):  # creating dict
    my_dict = {}
    commands = []
    texts = []
    text = ""
    for i in range(len(command_list[1:])):  # ignore E & P
        # get commands & options in a dict
        if command_list[1:][i].startswith("-"):
            commands.append(command_list[1:][i])
            if command_list[1:][i] == '-delpost':
                text = int(command_list[1:][i+1])  # get index
                texts.append(text)
                text = ""
            elif command_list[1:][i] == '-post':
                text = int(command_list[1:][i+1])  # get index
                texts.append(text)
                text = ""
            elif command_list[1:][len(command_list[1:])-1].startswith("-"):
                texts.append(text)  # text = "", last elem is command
            elif command_list[0] == "P":  # commands w no index in b/w
                texts.append(text)
            else:  # append the text after the command
                texts.append(command_list[1:][i+1])
        elif not command_list[1:][i].startswith("-") and not command_list[1:][i].isnumeric():
            text += " " + command_list[1:][i]  # still add in b/w entries
    my_dict = dict(zip(commands, texts))
    return my_dict


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


def whitespace_checker(text):
    return text.isspace() or text == "" or " " in text


def check_if_only_space(text):
    return text == "" or text.isspace()
