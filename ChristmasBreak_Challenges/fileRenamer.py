import os
import subprocess
from time import sleep

def getFileOrDirectory():
    directory = input("Full path of the file you want to rename")
    return directory

def rename():
    new_name = input("What would the new name be? ")
    try:
        os.rename(dir, new_name)
        print("File has been renamed")
        sleep(2)

    except FileExistsError:
        print("Name already exists")
        sleep(2)
        rename()

def main():
    getFileOrDirectory()
    rename()

    