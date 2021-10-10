#stock module imports
import tkinter as tk
from tkinter import *

#user-created imports
import webGen_gui
import webGen_functions
import webpage_generator


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

    #DEFINING THE MASTER FRAME CONFIG
        self.master = master
        self.master.minsize(200, 200) #(HEIGHT, WIDTH)
        self.master.maxsize(200, 200)
        

        #THIS 'CENTER_THE_WINDOW' METHOD WILL CENTER OUR APP TO THE USER'S SCREEN
        webGen_functions.center_the_window(self, 200, 200)
        self.master.title("Edit Webpage")
        self.master.configure(bg="#F0F0F0")
        

        #THIS PROTOCOL METHOD IS A TKINTER BUILT-IN METHOD TO CATCH IF THE USER CLICKS
        #ON THE UPPER RIGHT 'X' ON WINDOWS OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: webGen_functions.ask_whether_quit(self))
        arg = self.master


        #LOADING IN THE GUI WIDGETS FROM A SEPERATE MODULE,
        #KEEPING THE CODE COMPARTMENTALIZED AND CLUTTER-FREE
        webGen_gui.load_the_gui(self)




if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()