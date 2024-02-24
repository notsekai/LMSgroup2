from tkinter import *
import cv2
from time import *

class MenuWindow:
    def __init__(self, master):
        self.master = master
        self.menuFrame = Frame(master)
        self.menuFrame.pack()

        self.create_top_frame()
        self.create_gui()

    def create_top_frame(self):
        # Top frame for displaying title and time/date
        self.topFrame = Frame(self.master, width=1350, height=70, bg="#e1f8dc", padx=20, relief=SUNKEN, borderwidth=1)
        self.topFrame.pack(side=TOP, fill=X)

        # Label for displaying title and icon
        iconImage = PhotoImage(file='Library Manager\\icon.png')
        iconImage = iconImage.subsample(10)  # Adjust the size as needed
        self.topFrameLabel = Label(self.topFrame, text="EARL'S LIBRARY SYSTEM", relief=RAISED, 
                            bg='#e1f8dc', borderwidth=0, image=iconImage, compound=LEFT, font=('Trebuchet MS', 27, 'bold'))
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
        resized_image = cv2.resize(image, (500, 400))  # Adjust the size as needed

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

        # Frames for displaying various statistics
        frameTotalBooks = Frame (centerLeftFrame, bg='#EEDD82')
        frameTotalBooks.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

        # Label for displaying total number of books
        totalBooksBox = Label (frameTotalBooks, text=" Total Books: ", bg='#f9ba8e', width=14, height=3, font=('Trebuchet MS', 16, 'bold'))
        totalBooksBox.pack(side=RIGHT, anchor=NE, padx=10, pady=10)

        frameTotalAuthors = Frame (centerLeftFrame, bg='#EEDD82')
        frameTotalAuthors.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

        # Label for displaying total number of authors
        totalAuthorsBox = Label (frameTotalAuthors, text=" Total Authors: ", bg='#f9ba8e', width=14, height=3, font=('Trebuchet MS', 16, 'bold'))
        totalAuthorsBox.pack(side=RIGHT, anchor=NE, padx=10, pady=10)

        frameAvBooks = Frame (centerLeftFrame, bg='#EEDD82')
        frameAvBooks.pack(side=RIGHT, anchor=NW, padx=20, pady=20)

        # Label for displaying total number of available books
        totalAvBooksBox = Label (frameAvBooks, text=" Total Available Books: ", bg='#f9ba8e', width=19, height=4, font=('Trebuchet MS', 13, 'bold'))
        totalAvBooksBox.pack(side=RIGHT, anchor=NE, padx=10, pady=10)

        interface.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    root = Tk()
    menu = MenuWindow(root)
    root.mainloop()
