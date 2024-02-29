from tkinter import *
import cv2
from time import strftime
import json

class MenuWindow:
    def __init__(self, master):
        self.master = master
        self.menuFrame = Frame(master)
        self.menuFrame.pack()

        self.create_top_frame()
        self.load_data_from_json()
        self.create_gui()

    def create_top_frame(self):
        
        # Top frame for displaying title and time/date
        self.topFrame = Frame(self.master, width=1350, height=70, bg="#e1f8dc", padx=20, relief=SUNKEN, borderwidth=1)
        self.topFrame.pack(side=TOP, fill=X)

        # Label for displaying title and icon
        icon_image = PhotoImage(file='icon.png')
        icon_image = icon_image.subsample(10)  # Adjust the size as needed
        self.topFrameLabel = Label(self.topFrame, text=" EARL'S LIBRARY SYSTEM", relief=RAISED, 
                            bg='#e1f8dc', borderwidth=0, image=icon_image, compound=LEFT, font=('Trebuchet MS', 27, 'bold'))
        self.topFrameLabel.image = icon_image  # Keep a reference to the image
        self.topFrameLabel.pack(side=LEFT)

        # Label for displaying "Dashboard" text
        self.dashboardLabel = Label(self.topFrame, text="  Dashboard", relief=RAISED, 
                            bg='#e1f8dc', borderwidth=0, font=('Trebuchet MS', 17, 'bold'))
        self.dashboardLabel.pack(side=LEFT)

        # Labels for displaying time and date
        self.timeTopFrameLabel = Label(self.topFrame, font=('Trebuchet MS', 20, 'bold'), fg='black', bg='#e1f8dc')
        self.timeTopFrameLabel.pack(side=RIGHT)
        self.dateTopFrameLabel = Label(self.topFrame,font=('Trebuchet MS', 15, 'bold'), fg='black', bg='#e1f8dc')
        self.dateTopFrameLabel.pack(side=RIGHT, padx= 20)

        self.update()  # Start updating time and date

    def load_data_from_json(self):
        # Load data from JSON file
        with open('library_data.json', 'r') as file:
            self.data = json.load(file)

    def update_json_file(self):
        # Update JSON file with current data
        with open('library_data.json', 'w') as file:
            json.dump(self.data, file, indent=4)

    def update(self):
        # Update the time label with the current time
        time_string = strftime("%I:%M:%S %p")
        self.timeTopFrameLabel.config(text=time_string)

        # Update the date label with the current date
        date_string = strftime("%A, %B %d, %Y ")
        self.dateTopFrameLabel.config(text=date_string)
        # Schedule the update function to run again after 1 second
        self.master.after(1000, self.update)

    def create_gui(self):
        interface = self.master  # Creating a Tkinter window
        interface.title("Earl's Library System")
        interface.geometry("1200x625+200+200")  # Setting window dimensions
        interface.iconbitmap('Library manager\\icon.ico')  # Setting window icon

        # Read and resize the image using OpenCV
        image = cv2.imread('Library manager\\library.png')
        resized_image = cv2.resize(image, (570, 400))  # Adjust the size as needed

        # Convert the resized image to bytes
        resized_image_bytes = cv2.imencode('.png', resized_image)[1].tobytes()

        # Create a PhotoImage object from the bytes for displaying the library image
        libraryImage = PhotoImage(data=resized_image_bytes)

        ########################################## FRAMES ######################################################

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

        # Label for displaying the library image
        centerLeftFrameLabel = Label(centerLeftFrame, image=libraryImage)
        centerLeftFrameLabel.pack(side=BOTTOM, anchor=SE, padx=20, pady=7)

        # Load and resize the user image
        userImage = PhotoImage(file='Library manager\\user.png')
        userImage = userImage.subsample(2)  # Reduce the size

        # Label for displaying the user image and information
        centerRightFrameLabel = Label(centerRightFrame, image=userImage, compound=TOP, text="ADMIN", 
                                    font=('Trebuchet MS', 40 , 'bold'), padx=10, pady=10, bg="#ffd2b0", border=0)
        centerRightFrameLabel.pack()

        # Labels for displaying user information
        centerRightFrameLabel = Label(centerRightFrame, text="Luke Gabriel Arrieta\nSTAFF ID: 897-864-78", 
                                    font=('Trebuchet MS', 18 , 'bold'), padx=10, pady=10, bg="#ffd2b0", border=0)
        centerRightFrameLabel.pack()

        centerRightFrameLabel = Label(centerRightFrame, text="\n\n\nWVSU ID: M03471\nStatus: ACTIVE", font=('Trebuchet MS', 15 , 'bold'), padx=10, pady=2, bg="#ffd2b0", border=0)
        centerRightFrameLabel.pack()

        ###################################### SQUARE DISPLAYS ###################################

        # Frames for label of total books
        frameTotalBooks = Frame (centerLeftFrame, bg='#EEDD82')
        frameTotalBooks.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

        # Label for displaying total number of books
        totalBooks = len(self.data)
        totalBooksBox = Label (frameTotalBooks, text=f" Total Books: {totalBooks}", bg='#f9ba8e', width=15, height=3, font=('Trebuchet MS', 20, 'bold'))
        totalBooksBox.pack(side=RIGHT, anchor=NE, padx=10, pady=10)
        
        # Frame for displaying total number of authors
        frameTotalAuthors = Frame (centerLeftFrame, bg='#EEDD82')
        frameTotalAuthors.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

        # Counting the number of unique authors
        authors = set()  # Initializes an empty set to store unique authors
        #Iterate through each book in the data dictionary
        for book in self.data.values():
                authors.add(book['author'])  # Adds the author of each book to the set of authors

        totalAuthors = len(authors)  # Calculates the total number of unique authors by getting the length of the set

        # Label for displaying total number of authors
        totalAuthorsBox = Label (frameTotalAuthors, text=f" Total Authors: {totalAuthors}", bg='#f9ba8e', width=15, height=3, font=('Trebuchet MS', 20, 'bold'))
        totalAuthorsBox.pack(side=RIGHT, anchor=NE, padx=10, pady=10)

        # Counting the number of available books
        totalAvailableBooks = sum(1 for book in self.data.values() if book['available'])

        # Frame for displaying total available books
        frameAvBooks = Frame (centerLeftFrame, bg='#EEDD82')
        frameAvBooks.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

        # Label for displaying total number of available books
        totalAvBooksBox = Label (frameAvBooks, text=f" Total Available\nBooks: {totalAvailableBooks}", bg='#f9ba8e', width=19, height=4, font=('Trebuchet MS', 16, 'bold'))
        totalAvBooksBox.pack(side=RIGHT, anchor=NE, padx=10, pady=10)

        # Counting the number of checked out books
        totalCheckedOutBooks = sum(1 for book in self.data.values() if not book['available'])

        # Frame for displaying total number of books
        frameCheckoutBooks = Frame (centerLeftFrame, bg='#EEDD82')
        frameCheckoutBooks.place(x=20, y=150,)

        # Label for displaying total number of available books
        totalCheckoutBooks = Label (frameCheckoutBooks, text=f" Total Checked Out\nBooks: {totalCheckedOutBooks}", bg='#f9ba8e', width=18, height=3, font=('Trebuchet MS', 16, 'bold'))
        totalCheckoutBooks.pack(padx=10, pady=10)

        # Frame for displaying Notes / Reminders for Today
        reminderFrame = Frame (centerLeftFrame, bg='#EEDD82')
        reminderFrame.place(x=20, y=290)

        # Label for displaying total number of available books
        reminderLabel = Label (reminderFrame, text=" Reminder/Notes for Today ", bg='#EEDD82', fg='black', width=22, height=1, font=('Trebuchet MS', 13, 'bold'))
        reminderLabel.pack(padx=5, pady=10)
        reminderLabel.config(state=NORMAL)

        reminderText = Text (reminderFrame, width=27, height=10, font=('Trebuchet MS', 10, 'bold'))
        reminderText.pack(padx=5, pady=10)

        interface.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    root = Tk()
    menu = MenuWindow(root)
    root.mainloop()
