#stock module imports
import webbrowser

#user-created imports
import webGen_functions
import webGen_gui


#recieves the user input, updates the html file, and launches it in your browser
def generate(self):
    page = open("summerSale.html", 'w')
    updated_text = str(self.text_updatePage.get())

#apply the update
    page.write("<html> <body> <h1>" + updated_text + "</h1> </body> </html>")
    page.close()

#open the newly updated page
    webbrowser.open_new('summerSale.html')

#ensures this file is never ran as the main file
if __name__ == "__main__":
    pass

