from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import tkinter as tk
import os


import FT_PT2


reassigned = ''
##### MAIN #####
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        

        #DEFINING THE MASTER FRAME CONFIG
        self.master = master
        self.master.minsize(500, 300) #(HEIGHT, WIDTH)
        self.master.maxsize(500, 300)
        

        #THIS 'CENTER_THE_WINDOW' METHOD WILL CENTER OUR APP TO THE USER'S SCREEN
        center_the_window(self, 500, 300)
        self.master.title("File Scan And Transfer")
        self.master.configure(bg="#F0F0F0")
        

        #THIS PROTOCOL METHOD IS A TKINTER BUILT-IN METHOD TO CATCH IF THE USER CLICKS
        #ON THE UPPER RIGHT 'X' ON WINDOWS OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_whether_quit(self))
        arg = self.master


        #LOADING IN THE GUI WIDGETS FROM A SEPERATE MODULE,
        #KEEPING THE CODE COMPARTMENTALIZED AND CLUTTER-FREE
        load_the_gui(self)



##### GUI #####
def load_the_gui(self):
    self.button_browse1 = tk.Button(self.master, width=10, height=1, text='Browse...', command=lambda:callback(self))
    self.button_browse1.grid(row=0, column=0, padx=(27,0), pady=(20,0), sticky = N + W)

    self.text_path = tk.Entry(self.master, width=50, text='')
    self.text_path.grid(row=0, column=1, rowspan=1, columnspan=2, padx=(27, 0), pady=(20,0), sticky=N + E + W)

    self.button_reassign_destination = tk.Button(self.master, width=20, height=1, text='Assign Destination', command=lambda:FT_PT2.reassign_destination())
    self.button_reassign_destination.grid(row=1, column=0, padx=(27,0), pady=(20,0), sticky= N + W)

    self.button_init = tk.Button(self.master, width=12, height=2, text='Initiate Transfer', command=lambda:FT_PT2.transfer_initiate())
    self.button_init.grid(row=2, column=0, padx=(27,0),pady=(20,0), sticky=S + W)
    return self






##### FUNCTIONS #####
def center_the_window(self, w, h):

    #GETTING USER'S SCREEN WIDTH/HEIGHT
    the_screen_width = self.master.winfo_screenwidth()
    the_screen_height = self.master.winfo_screenheight()

    #CALCULATING X AND Y COORDINATES TO PAINT THE APP TO THE CENTER OF THE USER'S SCREEN
    x = int((the_screen_width/2) - (w/2))
    y = int((the_screen_height/2) - (h/2))
    centerGeometry = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeometry

def ask_whether_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #THIS WILL CLOSE THE APP
        self.master.destroy()
        os._exit(0)

#this updates the entry box and sends its contents to the other module via the "recieve_newPath" function
def callback(self):
    text = fd.askdirectory()
    self.text_path.delete(0, "end")
    self.text_path.insert(0, text)
    FT_PT2.recieve_newPath(text)
 









if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()