from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from LMSMenu import MenuWindow
import sys
import json

class LoginBackend:
    def __init__(self):
        self.user_data_file = 'user_data.json'
        self.load_user_data()

    def load_user_data(self):
        try:
            with open(self.user_data_file, 'r') as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            self.user_data = {}

    def save_user_data(self):
        with open(self.user_data_file, 'w') as file:
            json.dump(self.user_data, file, indent=4)

    def register(self, username, password):
        if not username or not password:
            messagebox.showerror("Error", "All fields are required.")
            return False

        if username in self.user_data:
            messagebox.showerror("Error", "Username already exists.")
            return False

        self.user_data[username] = password
        self.save_user_data()
        messagebox.showinfo("Success", "Registration successful.")
        return True

    def check(self, username, password):
        if username in self.user_data and self.user_data[username] == password:
            return True
        else:
            return False

class Login:
    def __init__(self, window):
        self.window = window
        self.login_backend = LoginBackend()
        self.frame = Frame(self.window, width=700, height=400)
        self.frame.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            sys.exit("Exiting application")

    def set_background_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        background_label = Label(self.frame, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = photo 

    def registerfn(self):
        username = self.namee_text.get()
        password = self.password1e_text.get()

        if self.login_backend.register(username, password):
            self.namee.delete(0, END)
            self.password1e.delete(0, END)

    def login_admin(self):
        username = self.namee_text.get()
        password = self.password1e_text.get()
        if self.login_backend.check(username, password):
            messagebox.showinfo("Login Successful", "Welcome! "+ username)
            self.window.destroy()
            openLMSMenu(self.window)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def loginfn(self):
        self.set_background_image('Library Manager//bgLogin.jpg')
        self.label = Label(self.frame, text='LOGIN', bg='White', fg='Black', font=('Tahoma', 24, 'bold'))
        self.label.place(x=245, y=35, width=150, height=60)

        self.name = Label(self.frame, text='Username:', bg='#D2B48C', fg= 'White', font=('Tahoma', 17, 'bold'))
        self.name.place(x=240, y=123, width=150, height=30)

        self.namee_text = StringVar()
        self.namee = Entry(self.frame, textvariable=self.namee_text, fg='gray', width=25, font=('Tahoma', 16, 'bold'))
        self.namee.place(x=215, y=161, width=200, height=30)

        self.password1 = Label(self.frame, text='Password :', bg='#D2B48C', fg='White',
                                font=('Tahoma', 17, 'bold'))
        self.password1.place(x=240, y=199, width=150, height=30)

        self.password1e_text = StringVar()
        self.password1e = Entry(self.frame, textvariable=self.password1e_text, bg='White', fg='gray', width=25,
                                 font=('Arial', 16, 'bold'), show='*')
        self.password1e.place(x=215, y=238, width=200, height=30)

        self.buttonlogin = Button(self.frame, text='LOGIN', bg='#6e93b0', fg='Black', font=('Tahoma', 18, 'bold'),
                                   cursor='hand2', command=self.login_admin)
        self.buttonlogin.place(x=60, y=300, width=200, height=50)

        self.buttonregister = Button(self.frame, text='REGISTER', bg='#6e93b0', fg='Black', font=('Tahoma', 18, 'bold'),
                                   cursor='hand2', command=self.registerfn)
        self.buttonregister.place(x=360, y=300, width=200, height=50)

def openLMSMenu(master):
    menu_window = Toplevel(master)
    menu_window.title("Menu")
    menu_window.geometry("400x300")
    menu = MenuWindow(menu_window)

if __name__ == "__main__":
    window = Tk()
    window.geometry("625x400")
    window.title("Earl's Library Login")
    window.iconbitmap('Library Manager//icon.ico')

    login_window = Login(window)
    login_window.loginfn()

    window.protocol("WM_DELETE_WINDOW", login_window.close_window)

    window.mainloop()
