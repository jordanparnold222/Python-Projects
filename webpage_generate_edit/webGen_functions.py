import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def ask_whether_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #THIS WILL CLOSE THE APP
        self.master.destroy()
        os._exit(0)

def center_the_window(self, w, h):
        #GETTING USER'S SCREEN WIDTH/HEIGHT
    the_screen_width = self.master.winfo_screenwidth()
    the_screen_height = self.master.winfo_screenheight()

    #CALCULATING X AND Y COORDINATES TO PAINT THE APP TO THE CENTER OF THE USER'S SCREEN
    x = int((the_screen_width/2) - (w/2))
    y = int((the_screen_height/2) - (h/2))
    centerGeometry = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeometry

#ensures this file is never ran as the main file
if __name__ == "__main__":
    pass