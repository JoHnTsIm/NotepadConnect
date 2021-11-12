from os.path import exists
from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk


class Login(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="#333")

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
        self.email_label = Label(self.frame, text="Email", bg="#333", fg="white", font="Helvetica 20")
        self.email_label.pack()

        # type your username
        self.email_entry = Entry(self.frame, bg="white", font="Verdana 15")
        self.email_entry.pack()

        # password label
        self.password_label = Label(self.frame, text="Password", bg="#333", fg="white", font="Helvetica 20")
        self.password_label.pack()

        # type your password
        self.password_entry = Entry(self.frame, bg="white", font="Verdana 15", show="*")
        self.password_entry.pack()

        # login button
        self.login_button = Button(self.frame, bg="#333", fg="white", text="Log In", font="Helvetica 20",
                                      command=self.check_user_entries)
        self.login_button.pack(pady=20)

        # self.label = Label(self.frame, text="You Don't Have An Account, Create One",
        #                    font="Helvetica 10", bg="#333", fg="white")
        # self.label.pack(side=BOTTOM)
        #
        # self.button = Button(self.frame, text="Register", font="Helvetica 10", bg="#333", fg="white")
        # self.button.pack(side=RIGHT)

    def assign_entries_to_variables(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        return email, password

    def current_user_data(self):
        email, password = self.assign_entries_to_variables()
        data_location = "user_data/" + str(email + ".txt")
        return data_location

    def check_user_entries(self):
        data_location = self.current_user_data()
        email, password = self.assign_entries_to_variables()
        if len(email) == 0 or len(password) == 0:
            messagebox.showwarning('Empty Field', 'A Field Is Empty!')

        elif exists(data_location):
            data = open(data_location, "r")
            data_lines = data.readlines()
            user_password = data_lines[1].replace("Password: ", "").replace("\n", "")

            if password == user_password:
                email_txt = open("shared_data.txt", "w")
                email_txt.write("logged in user: " + email)
                email_txt.close()
                messagebox.showinfo('Login Successful', 'You Have Logged In Successfully!')
                window.destroy()
                subprocess.call(['python', 'app.py'])

            else:
                messagebox.showinfo('Wrong Password', 'This Password Doesnt Match With This Email Address!')

        else:
            msgBox = messagebox.askquestion(title="User Doesnt Exists",
                                               message="This Email Address Doesnt Belong To Any User, Would You Like"
                                                       " To Create An Account With This Email Address?")
            if msgBox == "yes":
                window.destroy()
                subprocess.call(['python', 'register_user.py'])


if __name__ == "__main__":
    window = Tk()

    # Centering Tkinter Window
    window_height = 470
    window_width = 400

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ###########################

    window.title("NotepadConnect (Log In)")
    window.geometry("470x400")
    window.iconbitmap("notepad.ico")
    window.resizable(0, 0)

    Login(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
