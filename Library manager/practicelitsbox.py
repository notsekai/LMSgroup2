from tkinter import *

# Create Tkinter window
interface = Tk()
interface.title("Earl's Library System")
interface.geometry("1200x625+200+200")  # Setting window dimensions
interface.iconbitmap('Library manager\\icon.ico')  # Setting window icon

# Top frame for displaying title and time/date
topFrame = Frame(interface, width=1350, height=70, bg="#e1f8dc", padx=20, relief=SUNKEN, borderwidth=1)
topFrame.pack(side=TOP, fill=X)

# Label for displaying title
topFrameLabel = Label(topFrame, text="EARL'S LIBRARY SYSTEM", relief=RAISED, 
                    bg='#e1f8dc', borderwidth=0, font=('Trebuchet MS', 27, 'bold'))
topFrameLabel.pack(side=LEFT)

# Labels for displaying time and date
timeTopFrameLabel = Label(topFrame, font=('Trebuchet MS', 20, 'bold'), fg='black', bg='#e1f8dc')
timeTopFrameLabel.pack(side=RIGHT)
dateTopFrameLabel = Label(topFrame,font=('Trebuchet MS', 15, 'bold'), fg='black', bg='#e1f8dc')
dateTopFrameLabel.pack(side=RIGHT, padx= 20)

# Center frame for main content
centerFrame = Frame(interface, width=250, height=680, relief=RIDGE, bg="#ffd2b0")
centerFrame.pack(side=TOP)

# Left frame within center frame
centerLeftFrame = Frame(centerFrame, width=900, height=560, bg='#FEF8DD', borderwidth=2, relief=SUNKEN)
centerLeftFrame.pack(side=LEFT)
centerLeftFrame.pack_propagate(0)  # Prevent resizing

# Right frame within center frame
centerRightFrame = Frame(centerFrame, width=450, height=700, bg='#ffd2b0', borderwidth=1, relief=SUNKEN)
centerRightFrame.pack()

# Label for displaying the user information
centerRightFrameLabel = Label(centerRightFrame, text="ADMIN", 
                            font=('Trebuchet MS', 40 , 'bold'), padx=10, pady=10, bg="#ffd2b0", border=0)
centerRightFrameLabel.pack()

# Labels for displaying user information
centerRightFrameLabel = Label(centerRightFrame, text="Luke Gabriel Arrieta\nSTAFF ID: 897-864-78", 
                            font=('Trebuchet MS', 18 , 'bold'), padx=10, pady=10, bg="#ffd2b0", border=0)
centerRightFrameLabel.pack()

centerRightFrameLabel = Label(centerRightFrame, text="\n\n\nWVSU ID: M03471\nStatus: ACTIVE", font=('Trebuchet MS', 15 , 'bold'), padx=10, pady=2, bg="#ffd2b0", border=0)
centerRightFrameLabel.pack()

# Frames for label of total books
frameTotalBooks = Frame (centerLeftFrame, bg='#EEDD82')
frameTotalBooks.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

# Label for displaying total number of books
totalBooksBox = Label (frameTotalBooks, text=" Total Books: 0", bg='#f9ba8e', width=15, height=3, font=('Trebuchet MS', 20, 'bold'))
totalBooksBox.pack(side=RIGHT, anchor=NE, padx=10, pady=10)

# Frame for displaying total number of authors
frameTotalAuthors = Frame (centerLeftFrame, bg='#EEDD82')
frameTotalAuthors.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

# Label for displaying total number of authors
totalAuthorsBox = Label (frameTotalAuthors, text=" Total Authors: 0", bg='#f9ba8e', width=15, height=3, font=('Trebuchet MS', 20, 'bold'))
totalAuthorsBox.pack(side=RIGHT, anchor=NE, padx=10, pady=10)

# Frame for displaying total available books
frameAvBooks = Frame (centerLeftFrame, bg='#EEDD82')
frameAvBooks.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

interface.mainloop()  # Start the Tkinter event loop
