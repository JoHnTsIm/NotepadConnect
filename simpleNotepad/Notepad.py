import subprocess
from tkinter import *


class Notepad(object):
    def __init__(self):
        pass

    def login_register(self):
        global window
        window = Tk()
        window.title("Notepad (Log in/Register)")
        window.geometry('320x220')
        window.resizable(False, False)
        window.config(bg='#333')
        window.eval('tk::PlaceWindow . center')
        window.iconbitmap("Notepad-ico.ico")

        frame = Frame(window, bg='#333')
        frame.pack(pady=20)

        label = Label(frame, text="Notepad", font="Helvetica 30", bg='#333', fg="white")
        label.grid(row=1, column=1, columnspan=2, pady=20)

        button_login = Button(frame, text="Log In", bg='#333', fg="white", font="Helvetica 20", command=self.login)
        button_login.grid(row=2, column=1, padx=5)

        button_register = Button(frame, text="Register", bg='#333', fg="white", font="Helvetica 20",
                                 command=self.register)

        button_register.grid(row=2, column=2, padx=5)

        window.mainloop()

    def login(self):
        window.destroy()
        subprocess.call(['python', 'login.py'])

    def register(self):
        window.destroy()
        subprocess.call(['python', 'register.py'])


if __name__ == '__main__':
    Notepad().login_register()