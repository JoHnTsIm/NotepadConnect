
class Locate(object):

    # Opens the text file shared_data.txt on read only mode,
    # reads all the lines of this file, selects a specific line of text
    # more specific the first one that is current logged in user's email and last saves the location of the current
    # logged in user folder that has as folder name the current logged in user's email, then returns it
    @staticmethod
    def locate_user_folder():
        email = open("shared_data.txt", "r")

        lines = email.readlines()

        specific_line = lines[0].replace("logged in user: ", "")

        current_user_folder = "Users/" + str(specific_line + "/")

        return current_user_folder

    @staticmethod
    def empty_user_file_text():
        email = open("shared_data.txt", "w")

        email.truncate(0)

    @staticmethod
    def return_user_file():
        email = open("shared_data.txt", "r")

        lines = email.readlines()

        return lines
