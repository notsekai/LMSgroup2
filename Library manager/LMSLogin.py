from tkinter import *
from tkinter import messagebox

class LoginBackend:
    def check(self, username):
        messagebox.showinfo("Login Successful", "Welcome! "+ username)


class Login:
    def __init__(self, window):
        self.window = window
        self.login_backend = LoginBackend()

        self.frame = Frame(self.window, bg='Orange', width=700, height=400)

    def login_admin(self):
        username = self.namee_text.get()
        password = self.password1e_text.get()
        self.login_backend.check(username, password)
        self.window.destroy()

    def loginfn(self):
        self.label = Label(self.frame, text='Log In', bg='Orange', font=('Georgia', 36, 'bold'))

        self.name = Label(self.frame, text='Enter User_Name: ', bg='Orange', font=('Arial', 18, 'bold'))

        self.namee_text = StringVar()
        self.namee = Entry(self.frame, textvariable=self.namee_text, fg='gray', width=25, font=('Arial', 16, 'bold'))

        self.password1 = Label(self.frame, text='Enter Password : ', bg='Orange', fg='Green',
                                font=('Arial', 18, 'bold'))

        self.password1e_text = StringVar()
        self.password1e = Entry(self.frame, textvariable=self.password1e_text, bg='White', fg='gray', width=25,
                                 font=('Arial', 16, 'bold'), show='*')

        self.buttonlogin = Button(self.frame, text='LOG IN', bg='gray', fg='gray12', font=('Georgia', 18, 'bold'),
                                   cursor='hand2', command=self.login_admin)

        self.label.place(x=40, y=40, width=200, height=80)

        self.name.place(x=100, y=140, width=240, height=60)

        self.namee.place(x=380, y=150, width=200, height=30)

        self.password1.place(x=85, y=220, width=240, height=30)

        self.password1e.place(x=380, y=215, width=200, height=30)

        self.buttonlogin.place(x=180, y=300, width=140, height=50)

        self.frame.pack()

if __name__ == "__main__":
    window = Tk()
    window.geometry("800x600")
    window.title("Login Window")

    login_window = Login(window)
    login_window.loginfn()

    window.mainloop()