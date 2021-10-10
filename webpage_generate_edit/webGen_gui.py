#modules
import tkinter as tk
from tkinter import *
import webbrowser

#user-defined modules
import webpage_edit_main
import webGen_functions
import webpage_generator

def load_the_gui(self):

    self.label1 = tk.Label(self.master, text="Enter your update below!")
    self.label1.grid(row=0, column=0, padx=(20,20), pady=(20,20), sticky= N + E + W + S)
#sends the new text to the 'generate' method within the 'webpage_generator' module
    self.button_generate = tk.Button(self.master, width=12, height=1, text="UPDATE", command= lambda:webpage_generator.generate(self))
    self.button_generate.grid(row=2, column=0, sticky= N + E + W + S)
#text box that the users type their desired updated text into
    self.text_updatePage = tk.Entry(self.master, text="")
    self.text_updatePage.grid(row=1, column=0, padx=(20,20),pady=(20,20), sticky= N + E + W + S)




#ensures this file is never ran as the main file
if __name__ == "__main__":
    pass