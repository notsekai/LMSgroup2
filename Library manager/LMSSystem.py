from tkinter import *
from tkinter import messagebox
from LMSMenu import MenuWindow
from LMSLogin import Login
import datetime
import json
import cv2

class Library:
    def __init__(self):
        try:
            with open('library_data.json', 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = {}

    def save_database(self):
        with open('library_data.json', 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, book_id):
        if title not in self.books:
            self.books[title] = {'author': author, 'book_id': book_id, 'borrower_name': 'N/A', 'available': True}
            self.save_database()
            messagebox.showinfo("Success", f"Book '{title}' by {author} added successfully!")
        else:
            messagebox.showerror("Error", "Book already exists in the library.")

    def checkout_book(self, title, borrower_name):
        if title in self.books:
            if self.books[title]['available']:
                self.books[title]['available'] = False
                due_date = datetime.datetime.now() + datetime.timedelta(days=14)  # Due in 14 days
                self.books[title]['due_date'] = due_date.strftime('%Y-%m-%d')  # Store due date as string
                self.books[title]['borrower_name'] = borrower_name  # Store borrower's name
                self.save_database()
                messagebox.showinfo("Success", f"Book '{title}' checked out successfully! Please return by {due_date.strftime('%Y-%m-%d')}.")
            else:
                messagebox.showerror("Error", "Sorry, this book is currently checked out.")
        else:
            messagebox.showerror("Error", "Book not found in the library.")

    def return_book(self, title):
        if title in self.books:
            if not self.books[title]['available']:
                self.books[title]['available'] = True
                self.books[title].pop('due_date', None)
                self.books[title]['borrower_name'] = 'N/A'
                self.save_database()
                messagebox.showinfo("Success", f"Book '{title}' returned successfully!")

                if self.is_overdue(title):
                    messagebox.showinfo("Overdue Fine", f"You have an overdue fine of ${self.calculate_fine(title)} for book '{title}'.")
            else:
                messagebox.showerror("Error", "This book is not checked out.")
        else:
            messagebox.showerror("Error", "Book not found in the library.")

    def is_overdue(self, title):
        if title in self.books and 'due_date' in self.books[title]:
            due_date = datetime.datetime.strptime(self.books[title]['due_date'], '%Y-%m-%d')
            return datetime.datetime.now() > due_date
        return False

    def calculate_fine(self, title):
        if self.is_overdue(title):
            days_overdue = (datetime.datetime.now() - datetime.datetime.strptime(self.books[title]['due_date'], '%Y-%m-%d')).days
            return 0.5 * days_overdue
        return 0
    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            self.save_database()
            messagebox.showinfo("Success", f"Book '{title}' removed successfully!")
        else:
            messagebox.showerror("Error", "Book not found in the library.")

    def display_all_books(self):
        if self.books:
            book_list = "\n".join([f"{title} by {details['author']} ({'Available' if details['available'] else 'Checked out'})" for title, details in self.books.items()])
            messagebox.showinfo("All Books", "All Books:\n" + book_list)
        else:
            messagebox.showinfo("No Books", "No books in the library.")

    def check_overdue_books(self):
        today = datetime.datetime.now()
        overdue_books = []
        for title, details in self.books.items():
            if not details['available'] and datetime.datetime.strptime(details['due_date'], '%Y-%m-%d') < today:
                overdue_books.append(title)
        if overdue_books:
            messagebox.showinfo("Overdue Books", "The following books are overdue:\n" + "\n".join(overdue_books))
            for title in overdue_books:
                fine = self.calculate_fine(title)
                borrower_name = self.books[title]['borrower_name']
                messagebox.showinfo(f"Overdue Fine for {borrower_name}", f"You have an overdue fine of ${fine} for book '{title}'.")
        else:
            messagebox.showinfo("No Overdue Books", "No books are currently overdue.")

def populate_listbox():
    listbox_books.delete(0, END)  # Clear the listbox

    # Format the book information and insert into the listbox
    for title, details in library.books.items():
        book_info = f"{title:<40} | {details['book_id']:<40} | {details['author']:<40}"
        listbox_books.insert(END, book_info)

def add_book_callback():
    title = entry_BookTitle.get()
    author = entryAuthor.get()
    book_id = entryID.get()
    if title and author and book_id:
        library.add_book(title, author, book_id)
        populate_listbox()  # Update the listbox after adding a new book
    else:
        messagebox.showerror("Error", "Please enter all fields: title, author, and book ID.")

def checkout_book_callback():
    title = entry_BookTitle.get()
    borrower_name = entry_BorrowerName.get()  # Fetch borrower name from the correct entry field
    if title and borrower_name:
        library.checkout_book(title, borrower_name)  # Pass borrower name
    else:
        messagebox.showerror("Error", "Please enter the title of the book and borrower name.")

def return_book_callback():
    title = entry_BookTitle.get()
    if title:
        library.return_book(title)
    else:
        messagebox.showerror("Error", "Please enter the title of the book.")

def remove_book_callback():
    title = entry_BookTitle.get()
    if title:
        library.remove_book(title)
        populate_listbox()  # Update the listbox after removing a book
    else:
        messagebox.showerror("Error", "Please enter the title of the book to remove.")

# Add a Boolean variable to track the visibility of the listbox
is_listbox_visible = False

def display_all_books_callback():
    global is_listbox_visible
    if is_listbox_visible:
        listbox_books.place_forget()  # Hide the listbox
        scrollbar.place_forget()  # Hide the scrollbar
        hscrollbar.place_forget()  # Hide the hscrollbar
        is_listbox_visible = False
    else:
        populate_listbox_sort_by_id()  # Populate and sort the listbox by book ID
        listbox_books.place(x=0, y=0, relwidth=1, relheight=1)  # Show the listbox at the original position
        scrollbar.place(relx=1, rely=0, relheight=1)  # Show the scrollbar at the original position
        hscrollbar.place(x=0, rely=1, relwidth=1)  # Show the hscrollbar at the original position
        is_listbox_visible = True

def check_overdue_books_callback():
    library.check_overdue_books()

library = Library()

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


def populate_listbox_sort_by_id():
    listbox_books.delete(0, END)  # Clear the listbox
    # Sort the books by book ID
    sorted_books = sorted(library.books.items(), key=lambda x: x[1]['book_id'])
    for title, details in sorted_books:
        # Use get method to handle cases where 'borrower_name' may not be present
        borrower_name = details.get('borrower_name', 'N/A')
        # Format book details into a table-like manner
        book_info = f"Title: {title.ljust(30)} | Author: {details['author'].ljust(24)} | Book ID: {details['book_id'].ljust(15)} | Borrower Name: {borrower_name.ljust(8)} | Status: {'Available' if details['available'] else 'Checked Out'}"
        listbox_books.insert(END, book_info)

def calculate_fine(self, title):
    if self.is_overdue(title):
        days_overdue = (datetime.datetime.now() - datetime.datetime.strptime(self.books[title]['due_date'], '%Y-%m-%d')).days
        return 1.5 * days_overdue
    return 0

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

# Create main window
m_window = Tk()
m_window.geometry("1250x750")
m_window.title("Earl's Library Management System")
m_window.config(bg="#E6CBAE")

# Initializing Images using OpenCV
addBook_cv_image = cv2.imread('Library manager\\addbook.png')
removeBook_cv_image = cv2.imread('Library manager\\removeBook.png')
checkoutBook_cv_image = cv2.imread('Library manager\\checkout.png')
displayBook_cv_image = cv2.imread('Library manager\\displaybook.png')
overdueBook_cv_image = cv2.imread('Library manager\\overdue.png')
returnBook_cv_image = cv2.imread('Library manager\\returnbook.png')
menu_cv_image = cv2.imread('Library manager\\menu.png')

# Resize images using OpenCV
addBook_resized_image = cv2.resize(addBook_cv_image, (50, 50)) 
removeBook_resized_image = cv2.resize(removeBook_cv_image, (50, 50)) 
checkoutBook_resized_image = cv2.resize(checkoutBook_cv_image, (50, 50)) 
displayBook_resized_image = cv2.resize(displayBook_cv_image, (50, 50)) 
overdueBook_resized_image = cv2.resize(overdueBook_cv_image, (50, 50)) 
returnBook_resized_image = cv2.resize(returnBook_cv_image, (50, 50)) 
menu_resized_image = cv2.resize(menu_cv_image, (50, 50)) 

# Convert images to bytes using OpenCV
addBook_resized_image_bytes = cv2.imencode('.png', addBook_resized_image)[1].tobytes()
removeBook_resized_image_bytes = cv2.imencode('.png', removeBook_resized_image)[1].tobytes()
checkoutBook_resized_image_bytes = cv2.imencode('.png', checkoutBook_resized_image)[1].tobytes()
displayBook_resized_image_bytes = cv2.imencode('.png', displayBook_resized_image)[1].tobytes()
overdueBook_resized_image_bytes = cv2.imencode('.png', overdueBook_resized_image)[1].tobytes()
returnBook_resized_image_bytes = cv2.imencode('.png', returnBook_resized_image)[1].tobytes()
menu_resized_image_bytes = cv2.imencode('.png', menu_resized_image)[1].tobytes()

# Create PhotoImage objects from the bytes
addBook_photo_image = PhotoImage(data=addBook_resized_image_bytes)
removeBook_photo_image = PhotoImage(data=removeBook_resized_image_bytes)
checkoutBook_photo_image = PhotoImage(data=checkoutBook_resized_image_bytes)
displayBook_photo_image = PhotoImage(data=displayBook_resized_image_bytes)
overdueBook_photo_image = PhotoImage(data=overdueBook_resized_image_bytes)
returnBook_photo_image = PhotoImage(data=returnBook_resized_image_bytes)
menu_photo_image = PhotoImage(data=menu_resized_image_bytes)

topFrame = Frame(m_window, width=1350, height=60, bg="#f3e9dc", padx=20, relief=RAISED, borderwidth=1)
topFrame.pack(side=TOP, fill=X)

# Label for displaying title and icon
icon_image = PhotoImage(file='icon.png')
icon_image = icon_image.subsample(10)  # Adjust the size as needed
topFrameLabel = Label(topFrame, text=" EARL'S LIBRARY SYSTEM", relief=RAISED, 
                            bg='#f3e9dc', borderwidth=0, image=icon_image, compound=LEFT, font=('Trebuchet MS', 27, 'bold'))
topFrameLabel.image = icon_image  # Keep a reference to the image
topFrameLabel.pack(side=LEFT)

# Button frames
frameButton1 = Frame(m_window, bg="#544541", width=30, height=100, padx=2, pady=1)
frameButton1.place(relx=0.02, rely=0.10)

frameButton2 = Frame(m_window, bg="#544541", width=30, height=100, padx=2, pady=1)
frameButton2.place(relx=0.02, rely=0.23)

frameButton3 = Frame(m_window, bg="#544541", width=30, height=100, padx=2, pady=1)
frameButton3.place(relx=0.02, rely=0.36)

frameButton4 = Frame(m_window, bg="#544541", width=30, height=100, padx=2, pady=1)
frameButton4.place(relx=0.02, rely=0.49)

frameButton5 = Frame(m_window, bg="#544541", width=30, height=100, padx=2, pady=1)
frameButton5.place(relx=0.02, rely=0.62)

frameButton6 = Frame(m_window, bg="#544541", width=30, height=100, padx=2, pady=1)
frameButton6.place(relx=0.02, rely=0.75)

frameButton7 = Frame(m_window, bg="#544541", width=30, height=100, padx=2, pady=1)
frameButton7.place(relx=0.02, rely=0.88)

# Buttons
AddBookbutton = Button(frameButton1, text="  Add Book", font=('Trebuchet MS', 20 , 'bold'), fg='white', command=add_book_callback, bg="#aab396", height=49, width=320, image=addBook_photo_image, compound=LEFT, relief=RAISED, anchor='w')
AddBookbutton.pack(fill=BOTH, expand=True)

RemoveBookbutton = Button(frameButton2, text="  Remove Book", font=('Trebuchet MS', 20 , 'bold'), fg='white', command=remove_book_callback, bg="#636e5f", height=49, width=320, image=removeBook_photo_image, compound=LEFT, relief=RAISED, anchor='w')
RemoveBookbutton.pack(fill=BOTH, expand=True)

CheckoutBookbutton = Button(frameButton3, text="  Check Out", font=('Trebuchet MS', 20 , 'bold'), fg='white', command=checkout_book_callback, bg="#aab396", height=49, width=320, image=checkoutBook_photo_image, compound=LEFT, relief=RAISED, anchor='w')
CheckoutBookbutton.pack(fill=BOTH, expand=True)

ReturningBooksbutton = Button(frameButton4, text="  Return Book", font=('Trebuchet MS', 20 , 'bold'), fg='white', command=return_book_callback, bg="#636e5f", height=49, width=320, image=returnBook_photo_image, compound=LEFT, relief=RAISED, anchor='w')
ReturningBooksbutton.pack(fill=BOTH, expand=True)

CheckOverdueBooksbutton = Button(frameButton5, text="  Overdue Books", font=('Trebuchet MS', 20 , 'bold'), fg='white', command=check_overdue_books_callback, bg="#aab396", height=49, width=320, image=overdueBook_photo_image, compound=LEFT, relief=RAISED, anchor='w')
CheckOverdueBooksbutton.pack(fill=BOTH, expand=True)

DisplayAllBooksbutton = Button(frameButton6, text="  Display all Book", font=('Trebuchet MS', 20 , 'bold'),fg='white', command=display_all_books_callback, bg="#636e5f", height=49, width=320, image=displayBook_photo_image, compound=LEFT, relief=RAISED, anchor='w')
DisplayAllBooksbutton.pack(fill=BOTH, expand=True)

MenuButton = Button(frameButton7, text="  Menu", font=('Trebuchet MS', 20 , 'bold'), fg='white', command=lambda: openLMSMenu(m_window), bg="#aab396", height=55, width=320, image=menu_photo_image, compound=LEFT, relief=RAISED, anchor='w')
MenuButton.pack(fill=BOTH, expand=True)

# Frames
frameRight = Frame(m_window, bg='#CBB889', width=90, height=150 , padx=15, pady= 10)
frameRight.pack(side=RIGHT, anchor=NE, padx=15, pady=20)

ABFrame = Frame(m_window, bg='#f3e9dc', width=845, height=320 ,padx= 10, pady= 10, borderwidth=2)
ABFrame.place(relx=1.0, rely=1.0, x=-860, y=-425)

# Labels and entries
label_BookID = Label(frameRight, bg='#b58567', fg='white', height=1, width= 12, text="Book ID:", font= ('Helvetica', 15,'bold'), padx=5, pady=7, relief=RAISED)
label_BookID.grid(row=0,column=0)

entryID = Entry(frameRight, width= 52, font=('Helvetica', 14, 'bold'))
entryID.grid(row=0,column=1, padx= 20, pady=20)

label_Author = Label(frameRight, bg='#b58567', fg='white', text = "Author:", height=1, width= 12, font= ('Helvetica', 15,'bold'), padx=5, pady=7, relief=RAISED)
label_Author.grid(row=1,column=0,padx= 20, pady=20)

entryAuthor= Entry(frameRight, width= 52, font=('Helvetica', 14, 'bold'))
entryAuthor.grid(row=1,column=1, padx= 20, pady=20)

label_BookTitle = Label(frameRight, bg='#c68054', fg='white', height=1, width= 12, text="Book Title:", font= ('Helvetica', 15 ,'bold'), padx=5, pady=7, relief=RAISED)
label_BookTitle.grid(row=2,column=0, padx= 20, pady=20)

entry_BookTitle = Entry(frameRight, width= 52, font=('Helvetica', 14, 'bold'))
entry_BookTitle.grid(row=2,column=1, padx= 20, pady=20)

#########################NEW FRAME FOR BORROWER'S NAME#####################
frameBorrowerName = Frame(m_window, bg="#CCAE9A", width=90, height=100, padx=15, pady= 10)
frameBorrowerName.place(relx=1.0, rely=1.0, x=-860, y=-105)

label_BorrowerName = Label(frameBorrowerName, bg="#C08552", height=1, width= 12, text="Borrower Name:", font= ('Helvetica',15 ,'bold'), padx=5, pady=10, relief=RAISED)
label_BorrowerName.grid(row=0,column=0, padx= 10, pady=10)

entry_BorrowerName = Entry(frameBorrowerName, width= 54, font=('Helvetica', 14, 'bold'))
entry_BorrowerName.grid(row=0,column=1, padx=20, pady=20)

#########################LIST#####################
listbox_books = Listbox(ABFrame, width=90, height=15, font=('Courier New', 11))


####################### SCROLLBAR #######################
# Vertical scrollbar
scrollbar = Scrollbar(ABFrame, orient=VERTICAL)
scrollbar.config(command=listbox_books.yview)


# Horizontal scrollbar
hscrollbar = Scrollbar(ABFrame, orient=HORIZONTAL)
hscrollbar.config(command=listbox_books.xview)


listbox_books.config(yscrollcommand=scrollbar.set, xscrollcommand=hscrollbar.set)


m_window.mainloop()
