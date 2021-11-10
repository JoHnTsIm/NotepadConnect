from tkinter import *
import subprocess
from PIL import Image, ImageTk


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

    def login(self):
        window.destroy()
        subprocess.call(['python', 'loginUser.py'])

    def register(self):
        window.destroy()
        subprocess.call(['python', 'registerUser.py'])


if __name__ == "__main__":
    window = Tk()
    window.title("NotepadConnect (Log In/Register)")
    window.geometry("510x220")
    window.iconbitmap("notepad.ico")
    window.resizable(0, 0)
    window.eval('tk::PlaceWindow . center')

    Main(window).pack(side="top", fill="both", expand=True)
    window.mainloop()