from tkinter import *
import subprocess
from PIL import Image, ImageTk
from locate_data import Locate


class Main(Frame):
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

        self.frame = Frame(self, bg="#333")
        self.frame.pack()

        self.login_button = Button(self.frame, text="Log In", bg="#333", fg="white", font="Helvetica 25",
                                   command=self.login)
        self.login_button.pack(side=LEFT, pady=20, padx=10)

        self.register_button = Button(self.frame, text="Register", bg="#333", fg="white", font="Helvetica 25",
                                      command=self.register)

        self.register_button.pack(side=RIGHT)

        self.check_login()

    @staticmethod
    def check_login():
        file_lines = Locate().return_user_file()

        if len(file_lines) != 0:
            window.destroy()
            subprocess.call(['python', 'app.py'])

    @staticmethod
    def login():
        window.destroy()
        subprocess.call(['python', 'login_user.py'])

    @staticmethod
    def register():
        window.destroy()
        subprocess.call(['python', 'register_user.py'])


if __name__ == "__main__":
    window = Tk()

    # Centering Tkinter Window
    window_height = 220
    window_width = 510

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ###########################

    window.title("NotepadConnect (Log In/Register)")
    window.geometry("510x220")
    window.iconbitmap("notepad.ico")
    window.resizable(0, 0)

    Main(window).pack(side="top", fill="both", expand=True)
    window.mainloop()