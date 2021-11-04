import tkinter as tk
from os.path import exists
from tkinter import messagebox
import subprocess


class Login(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="#333")

        self.img = tk.PhotoImage(file="notepad.png")

        # the frame from all objects
        self.frame = tk.Frame(self, bg="#333")
        self.frame.pack()

        self.imglabel = tk.Label(self.frame, image=self.img, bg="#333")
        self.imglabel.grid(row=1, column=1, padx=3, pady=15)

        self.notepadlabel = tk.Label(self.frame, text="JT_Notepad", font="Helvetica 30", bg="#333", fg="white")
        self.notepadlabel.grid(row=1, column=2, padx=3)

        # username label
        self.email_label = tk.Label(self.frame, text="Email", bg="#333", fg="white", font="15")
        self.email_label.grid(row=2, column=1, pady=5)

        # type your username
        self.email_entry = tk.Entry(self.frame, bg="white", font="15")
        self.email_entry.grid(row=2, column=2)

        # password label
        self.password_label = tk.Label(self.frame, text="Password", bg="#333", fg="white", font="15")
        self.password_label.grid(row=3, column=1, pady=5)

        # type your password
        self.password_entry = tk.Entry(self.frame, bg="white", font="15")
        self.password_entry.grid(row=3, column=2)

        # login button
        self.login_button = tk.Button(self.frame, bg="#333", fg="white", text="Log In", font="Helvetica 15",
                                      command=self.user_check_login)
        self.login_button.grid(column=1, columnspan=2, row=4, pady=15)

    def user_check_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # new user's text file with data location
        data_location = "user_data/" + str(email + ".txt")

        # this continues if there is an empty field
        if len(email) == 0 or len(password) == 0:
            tk.messagebox.showinfo('Empty Field', 'A Field Is Empty!')

        # this continues if text file with this name exists in this location
        elif exists(data_location):
            data = open(data_location, "r")
            data_lines = data.readlines()
            user_password = data_lines[1].replace("Password: ", "").replace("\n", "")

            # this continues if the password typed by the user, is equal to the password of the user's typed email
            if password == user_password:
                email_txt = open("email.txt", "w")
                email_txt.write(email)
                email_txt.close()
                tk.messagebox.showinfo('Login Successful', 'You Have Logged In Successfully!')
                window.destroy()
                subprocess.call(['python', 'notepadApp.py'])

            else:
                tk.messagebox.showinfo('Wrong Password', 'This Password Doesnt Match With This Email Address!')

        else:
            msgBox = tk.messagebox.askquestion(title="User Doesnt Exists",
                                               message="This Email Address Doesnt Belong To Any User, Would You Like"
                                                       " To Create An Account With This Email Address?")
            if msgBox == "yes":
                window.destroy()
                subprocess.call(['python', 'registerUser.py'])


if __name__ == "__main__":
    window = tk.Tk()
    window.title("JT_Notepad Login")
    window.geometry("400x220")
    window.iconbitmap("notepad.ico")
    window.eval('tk::PlaceWindow . center')
    window.resizable(0, 0)

    Login(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
