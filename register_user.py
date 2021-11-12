import os
from os.path import exists
from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image,ImageTk


class Register(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="#333")

        # notepad image
        self.img = PhotoImage(file="notepad.png")

        # the frame from all objects
        self.frame = Frame(self, bg="#333")
        self.frame.pack()

        # Create a canvas
        self.canvas = Canvas(self.frame, height=100, width=470, bg="#333", bd=-2)
        self.canvas.pack()

        # Load an image in the script
        self.img = (Image.open("NotepadConnect2560-500.png"))

        # Resize the Image using resize method
        self.resized_image = self.img.resize((450, 85), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)

        # Add image to the Canvas Items
        self.canvas.create_image(10, 10, anchor=NW, image=self.new_image)

        # username label
        self.username_label = Label(self.frame, text="Username", bg="#333", fg="white", font="Helvetica 20")
        self.username_label.pack()

        # username entry
        self.username_entry = Entry(self.frame, font="Verdana 15")
        self.username_entry.pack()

        # password label
        self.password_label = Label(self.frame, text="Password", bg="#333", fg="white", font="Helvetica 20")
        self.password_label.pack()

        # password entry
        self.password_entry = Entry(self.frame, bg="white", font="Verdana 15", show="*")
        self.password_entry.pack()

        # email label
        self.password_label = Label(self.frame, text="Email", bg="#333", fg="white", font="Helvetica 20")
        self.password_label.pack()

        # email entry
        self.email_entry = Entry(self.frame, bg="white", font="Verdana 15")
        self.email_entry.pack()

        # register button
        self.register_button = Button(self.frame, bg="#333", fg="white", text="Register", font="Helvetica 20",
                                         command=self.check_user_entries)
        self.register_button.pack(pady=20)

    def assign_entries_to_variables(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        return username, password, email

    def new_user_folder(self):
        username, password, email = self.assign_entries_to_variables()
        user_files_location = "Users/" + str(email)
        return user_files_location

    def new_user_file(self):
        username, password, email = self.assign_entries_to_variables()
        user_files_location = self.new_user_folder()
        user_data = [str("Username: " + username + "\n"), str("Password: " + password + "\n"),
                     str("Email: " + email + "\n")]

        data_location = "user_data/" + str(email)

        new_user = open(data_location + ".txt", "w")

        os.mkdir(user_files_location)

        for data in user_data:
            new_user.write(data)
        new_user.close()

    def check_user_entries(self):
        username, password, email = self.assign_entries_to_variables()
        user_files_location = self.new_user_folder()

        if len(username) == 0 or len(password) == 0 or len(email) == 0:
            messagebox.showwarning('Empty Field', 'A Field Is Empty!')

        elif exists(user_files_location):
            msgBox = messagebox.askquestion(title="User Exists",
                                               message="A User with this email address already exists, "
                                                       "do you want to login with this email address?")
            if msgBox == "yes":
                window.destroy()
                subprocess.call(['python', 'login_user.py'])

        else:
            self.new_user_file()
            self.new_user_folder()
            messagebox.showinfo(message="New User Registered Successfully!", title="Register Successful")
            window.destroy()
            subprocess.call(['python', 'login_user.py'])


if __name__ == "__main__":
    window = Tk()

    # Centering Tkinter Window
    window_height = 480
    window_width = 400

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ###########################

    window.title("NotepadConnect (Register)")
    window.geometry("480x400")
    window.iconbitmap("notepad.ico")
    window.resizable(0, 0)

    Register(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
