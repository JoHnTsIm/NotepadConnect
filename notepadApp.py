import os
from tkinter import *
from tkinter import filedialog
from os.path import exists
from os import listdir


class App(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="#333")

        # tkinter Frame
        self.frame = Frame(self, bg="#333")
        self.frame.pack(expand=True, fill=BOTH)
        window.bind('<Control-s>', self.save_current_open_file)
        window.bind('<Control-Shift-S>', self.save_current_as)

        # tkinter Text
        self.text_area = Text(self.frame, height=1000, width=74, bg='#333', fg='white', font='BBEdit 14',
                              selectbackground="yellow", selectforeground="black", exportselection=0)
        self.text_area.pack(side="right", expand=True, fill=BOTH)

        # tkinter Listbox
        self.file_selector = Listbox(self.frame, bg="#333", fg="white", font="Verdana",
                                        selectforeground="black", selectbackground="#CCCC00", activestyle='none', selectmode=SINGLE)

        self.file_selector.bind('<Double-1>', self.file_db_click_function)
        self.file_selector.pack(expand=True, fill=BOTH, )

        # run on start functions
        self.not_saved()
        # self.autosave()
        self.load_user_files()

        # tkinter Button
        self.add_button = Button(self.frame, text="Add", font="15",
                                    command=self.add_text_file)
        self.add_button.pack(side="left", ipadx=3, ipady=5)

        # tkinter Button
        self.remove_button = Button(self.frame, text="Remove", font="15", command=self.remove_text_file)
        self.remove_button.pack(side="left", ipadx=13, ipady=5)

        # tkinter Button
        self.open_button = Button(self.frame, text="Rename", font="15")
        self.open_button.pack(side="right", ipadx=3, ipady=5)

        """Menu Bar"""
        # tkinter Menu -> Top of window navigation menu
        self.menubar = Menu(self)
        self.master.config(menu=self.menubar)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Save (Ctrl+s)", command=self.save_current_not_event)
        self.filemenu.add_command(label="Save As (Ctrl+Shift+s)", command=self.save_current_as_not_event)
        self.filemenu.add_command(label="Open")
        self.menubar.add_cascade(label="File", menu=self.filemenu)

    # Opens the text file email.txt on read only mode, reads all the lines of this file, selects a specific line of text
    # more specific the first one that is current logged in user's email and last saves the location of the current
    # logged in user folder that has as folder name the current logged in user's email, then returns it
    def locate_user_folder(self):
        email = open("email.txt", "r")

        lines = email.readlines()

        specific_line = lines[0]

        current_user_folder = "Users/" + str(specific_line + "/")

        return current_user_folder

    # runs the locate_user_folder() function then creates a list with all the files inside the previous selected folder,
    # deletes whatever is inside the listbox and last inserts all the files from the previous selected folder
    # inside the listbox
    def load_user_files(self):
        current_user_folder = self.locate_user_folder()

        file_list = listdir(current_user_folder)

        self.file_selector.delete(0, END)

        for file in file_list:
            self.file_selector.insert('end', file)

    # gets the active listbox selected element and returns it
    def locate_current_file(self):
        current_file = self.file_selector.get(ACTIVE)

        return current_file

    # runs the function locate_user_folder() then the locate_current_file(), merges the previous selected folder with
    # the previous selected file and does it a one whole file location, then returns it
    def locate_file_location(self):
        current_user_folder = self.locate_user_folder()

        current_file = self.locate_current_file()

        current_file_location = current_user_folder + current_file

        return current_file_location

    # adds a text file inside the previous selected folder
    def add_text_file(self):
        current_user_folder = self.locate_user_folder()

        file_number = 0

        basic_file = "Text Document.txt"

        while exists(current_user_folder + basic_file):
            file_number += 1

            if file_number == 0:

                basic_file = 'Text Document'

            else:
                basic_file = 'Text Document' + '(' + str(file_number) + ')' + ".txt"

        open(current_user_folder + basic_file, "w")

        self.add_on_listbox(basic_file)

    # inserts the new text file's name into the listbox
    def add_on_listbox(self, basic_file):
        self.file_selector.insert(END, basic_file)

    # removes a text file from previous selected folder
    def remove_text_file(self):
        selected = self.file_selector.curselection()

        current_user_folder = self.locate_user_folder()

        if not selected:
            file = self.file_selector.get("end")

            selected_file_location = current_user_folder + file

            os.remove(selected_file_location)

            self.remove_from_list_box()

        else:

            file = self.file_selector.get(ACTIVE)
            selected_file_location = current_user_folder + file
            os.remove(selected_file_location)
            self.remove_from_list_box()

    # removes a file's name from the listbox
    def remove_from_list_box(self):
        selected = self.file_selector.curselection()
        if not selected:
            self.file_selector.delete("end")
        else:
            self.file_selector.delete(selected)

    # runs multiple functions when you double click a file's name from the listbox
    def file_db_click_function(self, event):
        self.open_file()
        self.reading_file()
        self.writing_text()
        self.change_title()

    # change window's title to the current title + previous selected file
    def change_title(self):
        current_file = self.locate_current_file()
        window.title("NotepadConnect - " + current_file)

    # opens the previous selected file from file location on a read and write mode
    def open_file(self):
        current_file_location = self.locate_file_location()
        file = open(current_file_location, "r+")
        return file

    # reads the previous selected file
    def reading_file(self):
        file = self.open_file()
        read_file = file.read()
        return read_file

    # writes the text of the previous selected file into the tkinter Text area
    def writing_text(self):
        file = self.reading_file()
        self.text_area.delete('1.0', END)
        self.text_area.insert(END, file)

    # saves the changes on the text of the previous selected file if Ctrl+s gets pressed
    def save_current_open_file(self, event):
        file = self.open_file()

        text = self.text_area.get('1.0', 'end-1c')

        file.truncate(0)

        file.write(text)

    # saves the changes on the text of the previous selected file if the option File->Save from the tkinter Menu
    # on the top gets pressed
    def save_current_not_event(self):
        file = self.open_file()
        text = self.text_area.get('1.0', 'end-1c')
        file.truncate(0)
        file.write(text)

    # opens the file explorer and let's you choose the save location, the name and the extension of the file
    # that is gonna saved with the current typed text from tkinter Text inside if Ctrl+Shift+s gets pressed
    def save_current_as(self, event):
        files = [('Text Document (.txt)', '*.txt'),
                 ('Python Files (.py)', '*.py'),
                 ('All Files', '*.*')]
        path_to_save_as = str(filedialog.asksaveasfile(filetypes = files, defaultextension = files))
        save_location = path_to_save_as.replace("<_io.TextIOWrapper name='", "").replace("' mode='w' encoding='cp1253'>", "")
        text = self.text_area.get('1.0', 'end-1c')
        f = open(save_location, 'w')
        f.write(text)
        f.close()

    # opens the file explorer and let's you choose the save location, the name and the extension of the file
    # that is gonna saved with the current typed text from tkinter Text inside if the option
    # File->Save As get pressed from tkinter Menu on the top
    def save_current_as_not_event(self):
        files = [('All Files', '*.*'),
                 ('Python Files', '*.py'),
                 ('Text Document', '*.txt')]
        path_to_save_as = str(filedialog.asksaveasfile(filetypes = files, defaultextension = files))
        save_location = path_to_save_as.replace("<_io.TextIOWrapper name='", "").replace("' mode='w' encoding='cp1253'>", "")
        text = self.text_area.get('1.0', 'end-1c')
        f = open(save_location, 'w')
        f.write(text)
        f.close()

    # checks if the current selected file has any changes and if yes the title changes to title+*filename
    # if the file hasnt any changes or get's saved the title returns to title+filename without the (*)
    # and last if the none filename is selected from the listbox the title changes to just the title
    def not_saved(self):
        selected = self.file_selector.curselection()
        current_file = self.locate_current_file()
        if selected:
            opened_file = self.open_file()
            file_text = opened_file.read()
            text = self.text_area.get('1.0', 'end-1c')
            if file_text == text:
                window.title("NotepadConnect - " + current_file)
            else:
                window.title("NotepadConnect - " + "*" + current_file)
        elif not selected:
            window.title("NotepadConnect")
        self.after(100, self.not_saved)

    # (problematic function) runs the save_current_not_event() function on repeat after every 1.3 sec or 1300 ms
    # def autosave(self):
    #     selected = self.file_selector.curselection()
    #     if selected:
    #         self.save_current_not_event()
    #     self.after(1300, self.autosave)


# creates the gui window of the program
if __name__ == "__main__":
    window = Tk()
    window.title("NotepadConnect")
    window.geometry("1200x700")
    window.iconbitmap("notepad.ico")
    window.minsize(width=1100, height=600)
    App(window).pack(expand=True, fill=BOTH)
    window.mainloop()
