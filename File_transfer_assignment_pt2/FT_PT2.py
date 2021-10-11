import os
import os.path, time
import shutil
import datetime as dt
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#user-created imports
import transferGUI
from transferGUI import *
#global variables for use later
source = 'C:/Users/pjord/AppData/Local/Programs/Python/Python39/Tech Academy/File_transfer_assignments/File_transfer_assignment_pt2/created_modified/'
destination = 'C:/Users/pjord/AppData/Local/Programs/Python/Python39/Tech Academy/File_transfer_assignments/File_transfer_assignment_pt2/transfer_recieved/'
files = os.listdir(source)
reassigned = ''

#this is called on when the user clicks the 'browse' button. It stores that path for the time being
def recieve_newPath(path):
    global reassigned
    reassigned = path

#This is called on when someone clicks the "assign destination" button.
# #It loads up the new destination path for when they choose to execute
def reassign_destination():
    global destination
    global reassigned
    destination = reassigned + '/'
    print(destination)


#this function is called when the person clicks the "initiate transfer" button
def transfer_initiate():
    for i in files:
        number_of_files = 0
        modified_time = dt.datetime.fromtimestamp(os.path.getmtime(source + i))
        created_time = dt.datetime.fromtimestamp(os.path.getctime(source + i))
        today = dt.datetime.now().date()

        number_of_files = number_of_files + 1

        if (modified_time.date() == today) or (created_time.date() == today):
            shutil.move(source + i, destination)

        else:
            pass





#makes sure this file is never ran as main
if __name__ == "__main__":
    pass
