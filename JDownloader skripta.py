# my script for moving a bunch of files from a bunch of separate folders
# From JDownloader, I downloaded over a 1000 videos of my Youtube liked videos. THe problem is that all those files
# in each separate folder. THat is, I had over a 1000 folders where each one of them had one video. Then I wrote this
# script without knowing anything about the os module.
# This script moved all of my files from separate directories into a one big directory.

import os

os.chdir("C:\\Users\\Marko\\+ SAFE +\\")
print(os.getcwd())
my_dir = os.getcwd()

source = "C:\\Users\\Marko\\+ SAFE +\\"
destination = "C:\\Users\\Marko\\+ DESTINATION +\\"
file_source = ""

# getting the full file path in the directory ---> directory + file
for directory, sub_dir, file in os.walk(my_dir):
    # directory ---> str
    # sub_dir ---> list
    # file ---> list
    file_source = os.path.join(directory, "".join(file))  # converting it to a string and then joining it with the  directory to form the full file path
    file_source = file_source.replace("\\", ("\\" + "\\")) # converting it Windows file path

    move_destination = os.path.join(destination, "".join(file)) # converting it to a string and then joining it with
    # the  destination folder to form the full file path
    move_destination = move_destination.replace("\\", ("\\" + "\\"))  # converting it Windows file path
    print("THE SOURCE OF THE FILE: ",file_source)
    print("THE COPY DESTINATION OF THAT FILE: ", move_destination)
    print("*" * 150)
    try:
        if os.path.isfile(file_source):
            os.rename(file_source, move_destination)
    except FileExistsError:
        print("No file")
    except:
        print("something is wrong")




























