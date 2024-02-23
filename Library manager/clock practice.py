from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S")
    time_label.config(text=time_string)

window = Tk()

time_label = Label (window, font=('Times new Roman', 12), fg='white', bg='black')
time_label.pack()

update()
window.mainloop()