from tkinter import *

class MenuWindow:
    def __init__(self):
        self.MenuWindow = Tk()
        self.MenuWindow.geometry("1150x660")
        self.MenuWindow.title("Library Management System Menu")
        self.MenuWindow.config(bg="#FFD8B1")

        ################################
        menuFrame = Frame(self.MenuWindow)
        menuFrame.pack()
        ####################################
        menuLabel = Label(menuFrame,text="MENU")
        menuLabel.pack()



    def run(self):
        self.MenuWindow.mainloop()

