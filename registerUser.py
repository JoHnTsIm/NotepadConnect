import os
import tkinter as tk
from os.path import exists
from tkinter import messagebox
import subprocess


class Register(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="#333")

        # notepad image
        self.img = tk.PhotoImage(file="notepad.png")

        # the frame from all objects
        self.frame = tk.Frame(self, bg="#333")
        self.frame.pack()

        # App image title
        self.imglabel = tk.Label(self.frame, image=self.img, bg="#333")
        self.imglabel.grid(row=1, column=1, padx=3, pady=15)

        # App title
        self.notepadlabel = tk.Label(self.frame, text="JT_Notepad", font="Helvetica 30", bg="#333", fg="white")
        self.notepadlabel.grid(row=1, column=2, padx=3)

        # username label
        self.username_label = tk.Label(self.frame, text="Username", bg="#333", fg="white", font="15")
        self.username_label.grid(row=2, column=1, pady=5)

        # username entry
        self.username_entry = tk.Entry(self.frame, bg="white", font="15")
        self.username_entry.grid(row=2, column=2)

        # password label
        self.password_label = tk.Label(self.frame, text="Password", bg="#333", fg="white", font="15")
        self.password_label.grid(row=3, column=1, pady=5)

        # password entry
        self.password_entry = tk.Entry(self.frame, bg="white", font="15")
        self.password_entry.grid(row=3, column=2)

        # email label
        self.password_label = tk.Label(self.frame, text="Email", bg="#333", fg="white", font="15")
        self.password_label.grid(row=4, column=1, pady=5)

        # email entry
        self.email_entry = tk.Entry(self.frame, bg="white", font="15")
        self.email_entry.grid(row=4, column=2)

        # register button
        self.register_button = tk.Button(self.frame, bg="#333", fg="white", text="Register", font="Helvetica 15",
                                         command=self.user_check_register)
        self.register_button.grid(column=1, columnspan=2, row=5, pady=15)

    # gets and checks user's data
    def user_check_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        # new user's folder location
        user_files_location = "Users/" + str(email)

        # this continues if user exists
        if exists(user_files_location):
            msgBox = tk.messagebox.askquestion(title="User Exists",
                                               message="A User with this email address already exists, "
                                                       "do you want to login with this email address?")
            # this continues if user select Yes
            if msgBox == "yes":
                window.destroy()
                subprocess.call(['python', 'loginUser.py'])

        # this continues if user doesnt exists
        else:
            # all user data
            user_data = [str("Username: " + username + "\n"), str("Password: " + password + "\n"),
                         str("Email: " + email + "\n")]

            # new user's text file with data location
            data_location = "user_data/" + str(email)

            # creates a new text file with the new user data
            new_user = open(data_location + ".txt", "w")

            # creates a folder with the email of the new user
            os.mkdir(user_files_location)

            # writes all the data to the user's text file
            for data in user_data:
                new_user.write(data)
            new_user.close()

            # message that pops up if user register successful, closes current window and starts loginUser.py file
            tk.messagebox.showinfo(message="New User Registered Successfully!", title="Register Successful")
            window.destroy()
            subprocess.call(['python', 'loginUser.py'])


if __name__ == "__main__":
    window = tk.Tk()
    window.title("JT_Notepad Register")
    window.geometry("400x260")
    window.iconbitmap("notepad.ico")
    window.eval('tk::PlaceWindow . center')
    window.resizable(0, 0)

    Register(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
