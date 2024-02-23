from tkinter import *
from tkinter import messagebox
from LMSMenu import MenuWindow
from LMSLogin import LoginBackend, Login
import datetime
import json
import cv2

class Library:
    def __init__(self):
        try:
            with open('library_database.json', 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = {}

    def save_database(self):
        with open('library_database.json', 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, book_id, borrower_name):
        if title not in self.books:
            self.books[title] = {'author': author, 'book_id': book_id, 'borrower_name': borrower_name, 'available': True}
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
                # Clear borrower's name when book is returned
                self.books[title]['borrower_name'] = 'XXXX'
                self.save_database()
                messagebox.showinfo("Success", f"Book '{title}' returned successfully!")
            else:
                messagebox.showerror("Error", "This book is not checked out.")
        else:
            messagebox.showerror("Error", "Book not found in the library.")

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
        overdue_books = [title for title, details in self.books.items() if not details['available'] and details['due_date'] < today]
        if overdue_books:
            messagebox.showinfo("Overdue Books", "Overdue Books:\n" + "\n".join(overdue_books))
        else:
            messagebox.showinfo("No Overdue Books", "No books are currently overdue.")

def add_book_callback():
    title = entry_BookTitle.get()
    author = entryAuthor.get()
    book_id = entryID.get()
    borrower_name = entry_BookNum.get()  # Changed to borrower name
    if title and author and book_id and borrower_name:
        library.add_book(title, author, book_id, borrower_name)  # Pass borrower name
        populate_listbox()  # Update the listbox after adding a new book
    else:
        messagebox.showerror("Error", "Please enter all fields: title, author, book ID, and borrower name.")

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
        listbox_books.pack_forget()  # Hide the listbox
        scrollbar.pack_forget()  # Hide the scrollbar
        is_listbox_visible = False
    else:
        populate_listbox_sort_by_id()  # Populate and sort the listbox by book ID
        listbox_books.pack(side=LEFT, fill=BOTH, expand=True)  # Show the listbox
        scrollbar.pack(side=RIGHT, fill=Y)  # Show the scrollbar
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

def populate_listbox():
    listbox_books.delete(0, END)  # Clear the listbox
    for title, details in library.books.items():
        if not details['available']:
            # Display return date if book is checked out
            borrower_name = details.get('borrower_name', 'XXXX')  # Get borrower's name or default to 'XXXX'
            book_info = f"Title: {title} | Author: {details['author']} | Book ID: {details['book_id']} | Borrower Name: {borrower_name} | Due Date: {details['due_date']} | Status: Checked Out"
        else:
            # Display status as available if book is not checked out
            book_info = f"Title: {title} | Author: {details['author']} | Book ID: {details['book_id']} | Status: Available"
            # Exclude borrower's name if book is available
            borrower_name = ''  # Empty string if book is available
        listbox_books.insert(END, book_info)

def populate_listbox_sort_by_id():
    listbox_books.delete(0, END)  # Clear the listbox
    # Sort the books by book ID
    sorted_books = sorted(library.books.items(), key=lambda x: x[1]['book_id'])
    for title, details in sorted_books:
        # Updated book_info to include borrower's name
        book_info = f"Title: {title} | Author: {details['author']} | Book ID: {details['book_id']} | Borrower Name: {details['borrower_name']} | Status: {'Available' if details['available'] else 'Checked Out'}"
        listbox_books.insert(END, book_info)

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
m_window.config(bg="#FFD8B1")

# Initializing Images

addBook_image = PhotoImage(file='Library manager\\addbook.png')
removeBook_image = PhotoImage(file='Library manager\\removeBook.png')
checkoutbook_image = PhotoImage(file='Library manager\\checkout.png')
displayBook_image = PhotoImage(file='Library manager\\displaybook.png')
overdueBook_image = PhotoImage(file='Library manager\\overdue.png')
returnBook_image = PhotoImage(file='Library manager\\returnbook.png')
menu_image = PhotoImage(file='Library manager\\menu.png')


# Button frames
frameButton1 = Frame(m_window, bg="#f6a192", width=30, height=100, padx=2, pady=1)
frameButton1.place(relx=0.02, rely=0.03)

frameButton2 = Frame(m_window, bg="#f6a192", width=30, height=100, padx=2, pady=1)
frameButton2.place(relx=0.02, rely=0.17)

frameButton3 = Frame(m_window, bg="#f6a192", width=30, height=100, padx=2, pady=1)
frameButton3.place(relx=0.02, rely=0.31)

frameButton4 = Frame(m_window, bg="#f6a192", width=30, height=100, padx=2, pady=1)
frameButton4.place(relx=0.02, rely=0.45)

frameButton5 = Frame(m_window, bg="#f6a192", width=30, height=100, padx=2, pady=1)
frameButton5.place(relx=0.02, rely=0.59)

frameButton6 = Frame(m_window, bg="#f6a192", width=30, height=100, padx=2, pady=1)
frameButton6.place(relx=0.02, rely=0.73)

frameButton7 = Frame(m_window, bg="#f6a192", width=30, height=100, padx=2, pady=1)
frameButton7.place(relx=0.02, rely=0.87)

# Buttons
AddBookbutton = Button(frameButton1, command=add_book_callback, bg="#f6a192", height=2, width=28, text="Add Book", font=('Courier New', 14, 'bold'), 
                       fg="white", relief=SUNKEN,)
AddBookbutton.grid(row=0, column=0, padx=10, pady=10)

RemoveBookbutton = Button(frameButton2, command=remove_book_callback, bg="#f6a192", height=2, width=28, text="Remove Book", font=('Courier New', 14, 'bold'), 
                          fg="white", relief=SUNKEN,)
RemoveBookbutton.grid(row=0, column=0, padx=10, pady=10)

CheckoutBookbutton = Button(frameButton3, command=checkout_book_callback, bg="#f6a192", height=2, width=28, text="Checkout Book", font=('Courier New', 14, 'bold'), 
                            fg="white", relief=SUNKEN,)
CheckoutBookbutton.grid(row=0, column=0, padx=10, pady=10)

ReturningBooksbutton = Button(frameButton4, command=return_book_callback, bg="#f6a192", height=2, width=28, text="Returning Books", font=('Courier New', 14, 'bold'), 
                              fg="white", relief=SUNKEN,)
ReturningBooksbutton.grid(row=0, column=0, padx=10, pady=10)

CheckOverdueBooksbutton = Button(frameButton5, command=check_overdue_books_callback, bg="#f6a192", height=2, width=28, text="Check Overdue Books", font=('Courier New', 14, 'bold'),
                                  fg="white", relief=SUNKEN,)
CheckOverdueBooksbutton.grid(row=0, column=0, padx=10, pady=10)

DisplayAllBooksbutton = Button(frameButton6, command=display_all_books_callback, bg="#f6a192", height=2, width=28, text="Display All Books", font=('Courier New', 14, 'bold'), 
                               fg="white", relief=SUNKEN,)
DisplayAllBooksbutton.grid(row=0, column=0, padx=10, pady=10)

MenuButton = Button(frameButton7, command=lambda: openLMSMenu(m_window), bg="#f6a192", height=2, width=28, text="Menu", font=('Courier New', 14, 'bold'), 
                    fg="white", relief=SUNKEN,)
MenuButton.grid(row=0, column=0, padx=10, pady=10)

# Frames
frameRight = Frame(m_window, bg="#9bedff", width=90, height=200 , padx=15, pady= 10)
frameRight.pack(side=RIGHT, anchor=NE, padx=15, pady=20)

ABFrame = Frame(m_window, bg='pink', width=845, height=295 ,padx= 10, pady= 10)
ABFrame.place(relx=1.0, rely=1.0, x=-860, y=-457)

# Labels and entries
label_BookID = Label(frameRight, height=1, width= 12, text="Book ID:", font= ('Helvetica', 15,'bold'), padx=5, pady=10, relief=RAISED)
label_BookID.grid(row=0,column=0)

entryID = Entry(frameRight, width= 52, font=('Helvetica', 14, 'bold'))
entryID.grid(row=0,column=1, padx= 20, pady=20)

label_Author = Label(frameRight, text = "Author:", height=1, width= 12, font= ('Helvetica', 15,'bold'), padx=5, pady=10, relief=RAISED)
label_Author.grid(row=1,column=0,padx= 20, pady=20)

entryAuthor= Entry(frameRight, width= 52, font=('Helvetica', 14, 'bold'))
entryAuthor.grid(row=1,column=1, padx= 20, pady=20)

label_BookTitle = Label(frameRight, height=1, width= 12, text="Book Title:", font= ('Helvetica', 15 ,'bold'), padx=5, pady=10, relief=RAISED)
label_BookTitle.grid(row=2,column=0, padx= 20, pady=20)

entry_BookTitle = Entry(frameRight, width= 52, font=('Helvetica', 14, 'bold'))
entry_BookTitle.grid(row=2,column=1, padx= 20, pady=20)

#########################NEW FRAME FOR BORROWER'S NAME#####################
frameBorrowerName = Frame(m_window, bg="#acddde", width=90, height=200, padx=15, pady= 10)
frameBorrowerName.place(relx=1.0, rely=1.0, x=-860, y=-150)

label_BorrowerName = Label(frameBorrowerName, height=1, width= 12, text="Borrower Name:", font= ('Helvetica',15 ,'bold'), padx=5, pady=10, relief=RAISED)
label_BorrowerName.grid(row=0,column=0, padx= 20, pady=20)

entry_BorrowerName = Entry(frameBorrowerName, width= 52, font=('Helvetica', 14, 'bold'))
entry_BorrowerName.grid(row=0,column=1, padx=20, pady=20)

#########################LIST#####################
listbox_books = Listbox(ABFrame, width=90, height=15, font=('Courier New', 11))
scrollbar = Scrollbar(ABFrame, orient=VERTICAL)
scrollbar.config(command=listbox_books.yview)
listbox_books.config(yscrollcommand=scrollbar.set)

m_window.mainloop()

