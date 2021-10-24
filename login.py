from os.path import exists
from tkinter import *
from tkinter import messagebox
import subprocess
from tkinter import filedialog
from os.path import basename
import sys
import os

windowLogin = Tk()
windowLogin.geometry('320x220')
windowLogin.title('Login To Notepad')
windowLogin.config(bg="#333")
windowLogin.eval('tk::PlaceWindow . center')
windowLogin.iconbitmap("Notepad-ico.ico")


class Auth(object):
    def __init__(self, master):

        self.frame = Frame(master, bg="#333")
        self.frame.pack(pady=20)

        self.title_label = Label(self.frame, text="Notepad", bg="#333", fg="white", font="Helvetica 40")
        self.title_label.grid(row=1, column=1, columnspan=2)

        self.email_entry = Entry(self.frame, font="15")
        self.email_entry.grid(column=2, row=2, pady=5)

        self.email_label = Label(self.frame, text='Email: ', bg="#333", fg="white", font="15")
        self.email_label.grid(column=1, row=2)

        self.password_entry = Entry(self.frame, show="*", font="15")
        self.password_entry.grid(column=2, row=3, pady=5)

        self.password_label = Label(self.frame, text='Password: ', bg="#333", fg="white", font="15")
        self.password_label.grid(column=1, row=3)

        self.register_button = Button(self.frame, text="Login", command=self.login_data, font="15")
        self.register_button.grid(column=1, columnspan=2, row=4, pady=5)

    def login_data(self):
        global email
        password = self.password_entry.get()
        email = self.email_entry.get()
        self.check_login(email, password)

    def check_login(self, email, password):
        if len(password) == 0 or len(email) == 0:
            print("A Field or Fields Is Empty")
        elif exists("user_data" + "/" + str(email) + ".txt"):
            file = open("user_data" + "/" + str(email) + ".txt", "r")
            all_lines = file.readlines()
            spec_line = all_lines[3].replace("Password: ", "").replace("\n", "")
            if spec_line == password:
                messagebox.showinfo('Login Successful', 'You Have Logged In Successfully')
                windowLogin.destroy()
                self.notepad_starts()
            else:
                messagebox.showinfo('Wrong Password', 'Wrong Password!')

        else:
            MsgBox = messagebox.askquestion(title="Create New Account?",
                                            message="This Account Doesn't Exist, You Want To Create A New Account? ")
            if MsgBox == "yes":
                windowLogin.destroy()
                subprocess.call(['python', 'register.py'])

    def notepad_starts(self):
        global window
        window = Tk()
        window.geometry('600x400')
        window.title('Text Editor')
        window.eval('tk::PlaceWindow . center')
        window.iconbitmap("Notepad-ico.ico")

        # function that used whenever the program starts
        self.user_save()
        ################################################

        self.text_area = Text(window, height=1000, width=1000, bg='#333', fg='white', font='BBEdit 15')
        self.text_area.pack()

        self.menubar = Menu(window, bg='#333', fg='white')

        # Menu 1 (File)
        self.filemenu = Menu(self.menubar, tearoff=0, bg='#333', fg='white')
        self.filemenu.add_command(label='New', command=self.new_file)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save As', command=self.save_as)
        self.filemenu.add_command(label='Save', command=self.save)
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        # Menu 2 (Help)
        self.filemenu2 = Menu(self.menubar, tearoff=0, bg='#333', fg='white')
        self.filemenu2.add_command(label='Editor functions', command=self.functions)
        self.menubar.add_cascade(label='Help', menu=self.filemenu2)

        # Menu 3 (Themes)
        self.filemenu3 = Menu(self.menubar, tearoff=0, bg='#333', fg='white')
        self.filemenu3.add_command(label='Light Theme', command=self.light_theme)
        self.filemenu3.add_command(label='Dark Theme', command=self.dark_theme)
        self.menubar.add_cascade(label='Themes', menu=self.filemenu3)

        window.config(menu=self.menubar)

        # Quit window
        window.protocol("WM_DELETE_WINDOW", self.on_closing)

        window.mainloop()

    # desides while the program is closing if will run the save function or not and the ask the user
    # if he wants to save current progress or not. Choices: yes OR no
    def on_closing(self):
        if exists(save_location.replace("' mode='r' encoding='cp1253'>", "")):
            text = open(save_location.replace("' mode='r' encoding='cp1253'>", ""), 'r')
            txt = text.read()
            if txt != self.text_area.get('1.0', 'end-1c'):
                result = messagebox.askquestion("Save", "Do you want to save the changes?")
                if result == 'yes':
                    self.save()
                    sys.exit()
                elif result == 'no':
                    sys.exit()
            else:
                sys.exit()
        else:
            sys.exit()

    # function that change's the theme of the program to light theme
    def light_theme(self):
        self.text_area.config(bg='white', fg='black')

        self.menubar.config(bg='white', fg='black')

        # Menu 1 (File)
        self.filemenu.config(bg='white', fg='black')

        # Menu 2 (Help)
        self.filemenu2.config(bg='white', fg='black')

        # Menu 3 (Themes)
        self.filemenu3.config(bg='white', fg='black')

    # function that change's the theme of the program to dark theme
    def dark_theme(self):
        self.text_area.config(bg='#333', fg='white')

        self.menubar.config(bg='#333', fg='white')

        # Menu 1 (File)
        self.filemenu.config(bg='#333', fg='white')

        # Menu 2 (Help)
        self.filemenu2.config(bg='#333', fg='white')

        # Menu 3 (Themes)
        self.filemenu3.config(bg='#333', fg='white')

    # finds desktop location on windows and saves a .txt file (text file)
    def user_save(self):
        global save_location
        file_num = 0
        file_name = 'Text Document'
        save_location = "Users/" + str(email) + '/' + file_name + '.txt'
        while exists(save_location):
            file_num += 1
            if file_num == 0:
                file_name = 'Text Document'
            else:
                file_name = 'Text Document' + '(' + str(file_num) + ')'
            save_location = "Users/" + str(email) + '/' + file_name + '.txt'
        else:
            open(save_location, 'w')
        window.title('Text Editor - ' + basename(save_location))

    # saves the current progress of the .txt(text) file
    def save(self):
        text = self.text_area.get('1.0', 'end-1c')
        f = open(save_location.replace("' mode='r' encoding='cp1253'>", ""), 'w')
        f.write(text)

    # let you select where and with what name you want to save the current progress of the .txt(text) file
    def save_as(self):
        path_to_save_as = filedialog.asksaveasfilename(defaultextension='.txt', initialfile='my_text_file')
        text = self.text_area.get('1.0', 'end-1c')
        f = open(path_to_save_as, 'w')
        f.write(text)

    # select a file to open and display his text on the editor
    def open_file(self):
        desktop = ""
        global save_location
        OS = sys.platform
        if OS == "win32":
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        elif OS == "linux" or OS == "linux2":
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

        file_location = filedialog.askopenfile(initialdir=desktop)
        file_content = file_location.read()
        self.text_area.delete('1.0', END)
        self.text_area.insert(END, file_content)
        save_location = str(file_location).replace("<_io.TextIOWrapper name='", "")\
            .replace("' mode='r' encoding='UTF-8'>", "")
        file = basename(str(file_location).replace("' mode='r' encoding='UTF-8'>", ""))
        window.title('Text Editor - ' + basename(save_location.replace("' mode='r' encoding='cp1253'>", "")))

    # creates new .txt file on desktop
    def new_file(self):
        self.user_save()
        self.text_area.delete('1.0', END)

    def functions(self):
        window2 = Tk()
        window2.title('Text Editor > Help')
        window2.eval('tk::PlaceWindow . center')
        window2.iconbitmap("Notepad-ico.ico")

        frame = Frame(window2, bg='#333')
        frame.pack()

        # Save As
        save_as_label = Label(frame, text='| Save As |', fg='white', bg='#333', font='12')
        save_as_text = Label(frame, text="'File -> Save As' opens file explorer and let's you choose "
                                         "\n where to save the text that you have currently typed "
                                         "\n as a text file (.txt), let's you choose the name of the file too",
                             fg='white', bg='#333')
        save_as_label.grid(row=1, column=1, pady=10)
        save_as_text.grid(row=2, column=1)

        # Save
        save_label = Label(frame, text='| Save |', fg='white', bg='#333', font='12')
        save_text = Label(frame, text="'File -> Save' saves the current text even if its empty, "
                                      "\n to the desktop as a .txt file", fg='white', bg='#333')
        save_label.grid(row=1, column=2, pady=10)
        save_text.grid(row=2, column=2)

        # Open
        open_label = Label(frame, text='| Open |', fg='white', bg='#333', font='12')
        open_text = Label(frame, text="'File -> Open' opens file explorer and let you choose a .txt file \n"
                                      "of your choice to open and see what is typed in it", fg='white', bg='#333')
        open_label.grid(row=3, column=1, pady=10)
        open_text.grid(row=4, column=1)

        # New
        new_label = Label(frame, text='| New |', fg='white', bg='#333', font='12')
        new_text = Label(frame, text="'File -> New' creates a new .txt (text) file on current user folder"
                         , fg='white', bg='#333')
        new_label.grid(row=3, column=2, pady=10)
        new_text.grid(row=4, column=2)

        light_theme_label = Label(frame, text='| Light Theme |', fg='white', bg='#333', font='15')
        light_theme_text = Label(frame, text="'Themes -> Light Theme' enables the light theme of the program, \n"
                                             "the light theme contains white background and black text", fg='white',
                                 bg='#333')
        light_theme_label.grid(row=5, column=1, pady=10)
        light_theme_text.grid(row=6, column=1)

        dark_theme_label = Label(frame, text='| Dark Theme |', fg='white', bg='#333', font='15')
        dark_theme_text = Label(frame, text="'Themes -> Dark Theme' enables the dark theme of the program, \n"
                                            "the dark theme contains dark background and white text",
                                fg='white', bg='#333')
        dark_theme_label.grid(row=5, column=2, pady=10)
        dark_theme_text.grid(row=6, column=2)

        window2.mainloop()


mainGUI = Auth(windowLogin)

windowLogin.mainloop()