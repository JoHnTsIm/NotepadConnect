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

        # contains the files of the current folder
        self.file_selector = tk.Listbox(self.frame, bg="#333", fg="white", font="Verdana")
        self.file_selector.bind('<Double-1>', self.change_title)
        self.file_selector.pack(side="top", ipadx=30, ipady=185)

        self.load_user_files()

        # button with text 'Add'
        self.add_button = tk.Button(self.frame, text="Add", font="15",
                                    command=self.add_text_file)
        self.add_button.pack(side="left", ipadx=3, ipady=5)

        # button with text 'Remove'
        self.remove_button = tk.Button(self.frame, text="Remove", font="15", command=self.remove_text_file)
        self.remove_button.pack(side="left", ipadx=5, ipady=5)

        # button with text 'Open'
        self.open_button = tk.Button(self.frame, text="Open", font="15")
        self.open_button.pack(side="right", ipadx=3, ipady=5)

    def locate_user_folder(self):
        email = open("email.txt", "r")
        lines = email.readlines()
        specific_line = lines[0]
        current_user_folder = "Users/" + str(specific_line + "/")
        return current_user_folder

    def load_user_files(self):
        current_user_folder = self.locate_user_folder()
        file_list = listdir(current_user_folder)

        self.file_selector.delete(0, tk.END)

        for file in file_list:
            self.file_selector.insert(0, file)

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

    def add_on_listbox(self, basic_file):
        self.file_selector.insert(tk.END, basic_file)

    def remove_text_file(self):
        current_user_folder = self.locate_user_folder()
        file = self.file_selector.get(tk.ACTIVE)
        selected_file_location = current_user_folder + file
        os.remove(selected_file_location)
        self.remove_from_list_box()

    def remove_from_list_box(self):
        selected = self.file_selector.curselection()
        self.file_selector.delete(selected)

    def change_title(self, event):
        current_file = self.file_selector.get(tk.ACTIVE)
        print(current_file)
        window.title("JT_Notepad - " + current_file)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("JT_Notepad")
    window.geometry("1000x600")
    window.iconbitmap("notepad.ico")
    window.resizable(0, 0)

    App(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
