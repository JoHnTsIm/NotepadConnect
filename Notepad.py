import tkinter as tk
import subprocess


class Main(tk.Frame):
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

        self.frame = tk.Frame(self, bg="#333")
        self.frame.pack()

        self.login_button = tk.Button(self.frame, text="Log In", bg="#333", fg="white", font="Verdana 25",
                                      command=self.login)
        self.login_button.grid(row=1, column=1, padx=20)

        self.register_button = tk.Button(self.frame, text="Register", bg="#333", fg="white", font="Verdana 25",
                                         command=self.register)
        self.register_button.grid(row=1, column=2, padx=20, pady=20)

    def login(self):
        window.destroy()
        subprocess.call(['python', 'loginUser.py'])

    def register(self):
        window.destroy()
        subprocess.call(['python', 'registerUser.py'])


if __name__ == "__main__":
    window = tk.Tk()
    window.title("JT_Notepad")
    window.geometry("400x220")
    window.iconbitmap("notepad.ico")
    window.resizable(0, 0)
    window.eval('tk::PlaceWindow . center')

    Main(window).pack(side="top", fill="both", expand=True)
    window.mainloop()