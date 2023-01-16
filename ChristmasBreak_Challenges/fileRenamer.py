import os
import subprocess
from time import sleep

def getFileOrDirectory():
    directory = input("Full path of the file you want to rename: ")
    return directory

def rename(directory):
    new_name = input("New name of the file: ")
    dest = f"./{new_name}"
    try:
        os.rename(directory, dest)
        print("File has been renamed")
        sleep(2)

    except FileExistsError:
        print("Name already exists")
        sleep(2)
        rename()

def main():
    rename(getFileOrDirectory())

main()