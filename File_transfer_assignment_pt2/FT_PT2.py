import os, sys
import os.path, time
import shutil
import datetime as dt
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
#user-created imports
import transferGUI
from transferGUI import *
#global variables for use later





def choose_source(self):
    src = filedialog.askdirectory()
    self.text_pathSource.insert(0, src)

def choose_dest(self):
    src = filedialog.askdirectory()
    self.text_pathDest.insert(0, src)
#this function is called when the person clicks the "initiate transfer" button
def transfer_initiate(self):
    source = self.text_pathSource.get()
    destination = self.text_pathDest.get()
    file = os.listdir(source)
    for i in file:
        modified_time = dt.datetime.fromtimestamp(os.path.getmtime(source + '/' + i))
        created_time = dt.datetime.fromtimestamp(os.path.getctime(source + '/' + i))
        today = dt.datetime.now()
        twenty_four = today - dt.timedelta(hours=24)

        if (modified_time > twenty_four):
            shutil.move(source + '/' + i, destination)

        else:
            pass





#makes sure this file is never ran as main
if __name__ == "__main__":
    pass
