import os
import tkinter as tk
from os.path import exists
from os import listdir


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(bg="#333")

        # the frame from all objects
        self.frame = tk.Frame(self, bg="#333")
        self.frame.pack()

        # type text here
        self.text_area = tk.Text(self.frame, height=1000, width=74, bg='#333', fg='white', font='BBEdit 15')
        self.text_area.pack(side="right")
        self.text_area.bind('<Control-s>', self.run_save_current_open_file_if)

        # contains the files of the current folder
        self.file_selector = tk.Listbox(self.frame, bg="#333", fg="white", font="Verdana",
                                        selectforeground="black", selectbackground="#CCCC00")
        self.file_selector.bind('<Double-1>', self.file_db_click_function)
        self.file_selector.pack(side="top", ipady=185)

        self.load_user_files()

        # button with text 'Add'
        self.add_button = tk.Button(self.frame, text="Add", font="15",
                                    command=self.add_text_file)
        self.add_button.pack(side="left", ipadx=3, ipady=5)

        # button with text 'Remove'
        self.remove_button = tk.Button(self.frame, text="Remove", font="15", command=self.remove_text_file)
        self.remove_button.pack(side="left", ipadx=13, ipady=5)

        # button with text 'Open'
        self.open_button = tk.Button(self.frame, text="Open", font="15", command=self.run_save_current_open_file_if)
        self.open_button.pack(side="right", ipadx=3, ipady=5)

    # opens and reads the email.txt file to check the email of the current 'Logged In User' and then saves the
    # location of his folder to a variable and then returns it
    def locate_user_folder(self):
        email = open("email.txt", "r")
        lines = email.readlines()
        specific_line = lines[0]
        current_user_folder = "Users/" + str(specific_line + "/")
        return current_user_folder

    # creates a list with all the files inside the selected folder with the listdir(not my function) function,
    # the insert that list to the listbox
    def load_user_files(self):
        current_user_folder = self.locate_user_folder()
        file_list = listdir(current_user_folder)

        self.file_selector.delete(0, tk.END)

        for file in file_list:
            self.file_selector.insert(0, file)

    # gives a basic name file to the first file and creates a file with that basic name, then if needing to create
    # another file checks if the current file exists and just adds one to the name of the next created file
    # e.g Text Document.txt, Text Document(1).txt, Text Document(2).txt...
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

    # adds file on the listbox
    def add_on_listbox(self, basic_file):
        self.file_selector.insert(tk.END, basic_file)

    # removes file from the folder
    def remove_text_file(self):
        current_user_folder = self.locate_user_folder()
        file = self.file_selector.get(tk.ACTIVE)
        selected_file_location = current_user_folder + file
        os.remove(selected_file_location)
        self.remove_from_list_box()

    # removes file from listbox
    def remove_from_list_box(self):
        selected = self.file_selector.curselection()
        self.file_selector.delete(selected)

    # do multiple functions with a double click on a listboxe's file
    def file_db_click_function(self, event):
        self.open_file()
        self.reading_file()
        self.writing_file_text_to_text_area()
        self.change_title()

    # change the window title to the current's selected file from the listbox
    def change_title(self):
        current_file = self.file_selector.get(tk.ACTIVE)
        window.title("JT_Notepad - " + current_file)

    # opens the selected listbox file and returns it on read and write mode
    def open_file(self):
        current_file = self.file_selector.get(tk.ACTIVE)
        current_user_folder = self.locate_user_folder()
        file = open(current_user_folder + current_file, "r+")
        return file

    # reading current's selected file text
    def reading_file(self):
        file = self.open_file()
        read_file = file.read()
        return read_file

    # writing current's selected file text to the text area
    def writing_file_text_to_text_area(self):
        file = self.reading_file()
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, file)

    # saves the text from the text area to the current selected file
    def save_current_open_file(self):
        file = self.open_file()
        text = self.text_area.get('1.0', 'end-1c')
        file.write(text)

    # checks if the text in the file is different from the on the text area and if its true
    # runs save_current_open_file function
    def run_save_current_open_file_if(self, event):
        file = self.open_file()
        file_text = file.read()
        text = self.text_area.get('1.0', 'end-1c')
        if file_text != text:
            self.save_current_open_file()

    # trying to do autosave whenever change selected object from listbox
    # def autosave(self):
    #     file = self.open_file()
    #     file_text = file.read()
    #     text = self.text_area.get('1.0', 'end-1c')
    #     if file_text != text:
    #         self.save_current_open_file()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("JT_Notepad")
    window.geometry("1020x600")
    window.iconbitmap("notepad.ico")
    window.resizable(0, 0)

    App(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
