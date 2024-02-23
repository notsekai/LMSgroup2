from tkinter import *
from tkinter import messagebox
import cv2
from LMSMenu import MenuWindow
from LMSLogin import LoginBackend, Login

def openLMSMenu(master):
    # Create an instance of MenuWindow
    menu_window = Toplevel(master)
    menu_window.title("Menu")
    menu_window.geometry("400x300")

    # Instantiate the MenuWindow class
    menu = MenuWindow(menu_window)

def loginBackend(login_window):
    # Initialize the Login object
    login = Login(login_window)
    login.loginfn()

def main():
    # Create a new Tkinter window for login
    login_window = Tk()
    login_window.geometry("800x600")
    login_window.title("Login Window")

    # Run the login window
    loginBackend(login_window)
    login_window.mainloop()

if __name__ == "__main__":
    main()

################## WINDOW ################
m_window = Tk()
m_window.geometry("1150x730")
m_window.title("Library Management System")
m_window.config(bg="#FFD8B1")

###################### BUTTON FRAMES ###########################
frameButton1 = Frame(m_window, bg="#f6a192", width=30, height= 100,padx= 2, pady= 2)
frameButton1.place(relx=0.05, rely=0.03)

frameButton2 = Frame(m_window, bg="#f6a192", width=30, height= 100,padx= 1, pady= 1)
frameButton2.place(relx=0.05, rely=0.18)

frameButton3 = Frame(m_window, bg="#f6a192", width=30, height= 100,padx= 1, pady= 1)
frameButton3.place(relx=0.05, rely=0.33)

frameButton4 = Frame(m_window, bg="#f6a192", width=30, height= 100,padx= 1, pady= 1)
frameButton4.place(relx=0.05, rely=0.48)

frameButton5 = Frame(m_window, bg="#f6a192", width=30, height= 100,padx= 1, pady= 1)
frameButton5.place(relx=0.05, rely=0.61)

frameButton6 = Frame(m_window, bg="#f6a192", width=30, height= 100,padx= 1, pady= 1)
frameButton6.place(relx=0.05, rely=0.76)

frameButton7 = Frame(m_window, bg="#f6a192", width=30, height= 100,padx= 1, pady= 1)
frameButton7.place(relx=0.05, rely=0.91)

############################# BUTTONS #########################
AddBookbutton = Button(frameButton1, bg="#f6a192", height=2, width=20, text="Add Book", font=('Courier New', 14, 'bold'), fg="white", relief=SUNKEN)
AddBookbutton.grid(row=0, column= 0,padx=2, pady=2)

RemoveBookbutton = Button(frameButton2, bg="#f6a192", height=2, width=20, text="Remove Book", font=('Courier New', 14, 'bold'), fg="white", relief=SUNKEN)
RemoveBookbutton.grid(row=0, column= 0,padx=2, pady=2)

CheckoutBookbutton = Button(frameButton3, bg="#f6a192", height=2, width=20, text="Checkout Book", font=('Courier New', 14, 'bold'), fg="white", relief=SUNKEN)
CheckoutBookbutton.grid(row=0, column= 0,padx=2, pady=2)

ReturningBooksbutton = Button(frameButton4, bg="#f6a192", height=2, width=20, text="Returning Books", font=('Courier New', 14, 'bold'), fg="white", relief=SUNKEN)
ReturningBooksbutton.grid(row=0, column= 0,padx=2, pady=2)

CheckOverdueBooksbutton = Button(frameButton5, bg="#f6a192", height=2, width=20, text="Check Overdue Books", font=('Courier New', 14, 'bold'), fg="white", relief=SUNKEN)
CheckOverdueBooksbutton.grid(row=0, column= 0,padx=2, pady=2)

DisplayAllBooksbutton = Button(frameButton6, bg="#f6a192", height=2, width=20, text="Display All Books", font=('Courier New', 14, 'bold'), fg="white", relief=SUNKEN)
DisplayAllBooksbutton.grid(row=0, column= 0,padx=2, pady=2)

MenuButton = Button(frameButton7, command=lambda: openLMSMenu(m_window), bg="#f6a192", height=2, width=20, text= "Menu", font=('Courier New', 14, 'bold'), fg="white", relief=SUNKEN)
MenuButton.grid(row=0, column= 0,padx=2, pady=2)

###################### FRAMES ###########################
frameRight = Frame(m_window, bg="#9bedff",width=100, height=200 ,padx= 10, pady= 10)
frameRight.pack(side=RIGHT, anchor=NE, padx=15, pady=20)

############################# LABEL #########################
label_BookID = Label(frameRight, height=1, width= 12, text="Book ID:", font= ('Helvetica', 15,'bold'), padx=5, pady=10, relief=RAISED)
label_BookID.grid(row=0,column=0)

entryID = Entry(frameRight, width= 42, font=('Helvetica', 14, 'bold'))
entryID.grid(row=0,column=1, padx= 20, pady=20)

label_Author = Label(frameRight, text = "Author:", height=1, width= 12, font= ('Helvetica', 15,'bold'), padx=5, pady=10, relief=RAISED)
label_Author.grid(row=1,column=0,padx= 20, pady=20)

entryAuthor= Entry(frameRight, width= 42, font=('Helvetica', 14, 'bold'))
entryAuthor.grid(row=1,column=1, padx= 20, pady=20)

label_BookTitle = Label(frameRight, height=1, width= 12, text="Book Title:", font= ('Helvetica', 15 ,'bold'), padx=5, pady=10, relief=RAISED)
label_BookTitle.grid(row=2,column=0, padx= 20, pady=20)

entry_BookTitle = Entry(frameRight, width= 42, font=('Helvetica', 14, 'bold'))
entry_BookTitle.grid(row=2,column=1, padx= 20, pady=20)

label_BookNum = Label(frameRight, height=1, width= 12, text="Book Number:", font= ('Helvetica',15 ,'bold'), padx=5, pady=10, relief=RAISED)
label_BookNum.grid(row=3,column=0, padx= 20, pady=20)

entry_BookNum = Entry(frameRight, width= 42, font=('Helvetica', 14, 'bold'))
entry_BookNum.grid(row=3,column=1, padx=20, pady=20)

######################### BUTTONS #############################
ButtonSubmit = Button(frameRight,text="Submit", height=2, width=10)
ButtonSubmit.grid(row=6,columnspan=2, pady=0, sticky=S)

m_window.mainloop()
