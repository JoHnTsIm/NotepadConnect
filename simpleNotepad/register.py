from os.path import exists
from tkinter import *
import subprocess
from tkinter import messagebox
from os import mkdir


class Auth(object):
    def __init__(self):
        pass

    def register_data(self):
        firstname = self.fname_entry.get()
        lastname = self.lname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        self.check_register(firstname, lastname, username, password, email)

    def check_register(self, firstname, lastname, username, password, email):
        file = ["First Name: " + firstname + "\n", "Last Name: " + lastname + "\n", "Username: " + username + "\n",
                "Password: " + password + "\n", "Email: " + email + "\n"]

        if len(firstname) == 0 or len(lastname) == 0 or len(username) == 0 or len(password) == 0 or len(email) == 0:
            print("A Field or Fields Is Empty")

        elif exists("user_data" + "/" + str(email) + ".txt"):
            MsgBox = messagebox.askquestion(title="User Already Exists",
                                            message="You Want To Login With Existing User")
            if MsgBox == "yes":
                windowRegister.destroy()
                subprocess.call(['python', 'login.py'])

        else:
            mkdir("Users/" + email)
            save_location = open("user_data" + "/" + str(email) + ".txt", "w")
            for data in file:
                save_location.write(data)
            messagebox.showinfo('User Registered', 'User Registered Successfully')
            save_location.close()
            windowRegister.destroy()
            subprocess.call(['python', 'login.py'])

    def register(self):
        global windowRegister
        windowRegister = Tk()
        windowRegister.title("Register To Notepad")
        windowRegister.eval('tk::PlaceWindow . center')
        windowRegister.config(bg="#333")
        windowRegister.geometry('320x220')
        windowRegister.iconbitmap("Notepad-ico.ico")

        self.frame = Frame(windowRegister, bg="#333")
        self.frame.pack(pady=10)

        self.fname_entry = Entry(self.frame, font="15")
        self.fname_entry.grid(column=2, row=1, pady=5)

        self.fname_label = Label(self.frame, text='First Name: ', bg="#333", fg="white", font="15")
        self.fname_label.grid(column=1, row=1)

        self.lname_entry = Entry(self.frame, font="15")
        self.lname_entry.grid(column=2, row=2, pady=5)

        self.lname_label = Label(self.frame, text='Last Name: ', bg="#333", fg="white", font="15")
        self.lname_label.grid(column=1, row=2)

        self.username_entry = Entry(self.frame, font="15")
        self.username_entry.grid(column=2, row=3, pady=5)

        self.username_label = Label(self.frame, text='Username: ', bg="#333", fg="white", font="15")
        self.username_label.grid(column=1, row=3)

        self.password_entry = Entry(self.frame, show="*", font="15")
        self.password_entry.grid(column=2, row=4, pady=5)

        self.password_label = Label(self.frame, text='Password: ', bg="#333", fg="white", font="15")
        self.password_label.grid(column=1, row=4)

        self.email_entry = Entry(self.frame, font="15")
        self.email_entry.grid(column=2, row=5, pady=5)

        self.email_label = Label(self.frame, text='Email: ', bg="#333", fg="white", font="15")
        self.email_label.grid(column=1, row=5)

        self.register_button = Button(self.frame, text="Register", command=self.register_data, font="15")
        self.register_button.grid(column=1, columnspan=2, row=6, pady=5)

        windowRegister.mainloop()


if __name__ == '__main__':
    Auth().register()