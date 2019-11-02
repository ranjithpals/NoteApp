import sys
from Notebook import Notebook, Note


class Menu:
    """
    Display Menu options to user via Command Line to perform the Notebook operations
    """

    def __init__(self):
        """
        1. Initialize the Notebook instance
        2. Define the mapping for the menu and operations (methods) to be performed
        """
        self.notebook = Notebook()
        self.choices = {
                        "1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.modify_tags,
                        "6": self.quit
                        }

    # Static Method as it only used for display purpose and data operations performed.
    @staticmethod
    def display_menu():
        """
        Menu to be displayed to the user
        :return:
        """
        print("""
        
    Notebook Menu
    
    1. Show all Notes
    2. Search Notes
    3. Add Note
    4. Modify Note
    5. Modify Tags
    6. Quit
    
    """)

    def run(self):
        """
        Display the user menu and obtain the user input for the required operation
        :return:
        """
        self.display_menu()
        # Obtain user input
        choice = input("Enter an option: ")
        action = self.choices.get(choice)
        if action:
            action()
        else:
            print("{} is not a valid choice, please select a valid choice")

        # Call the menu again to continue additional operations
        self.run()

    def show_notes(self, notes=None, filter_key=False):
        """
        Display all the notes linked to the Notebook
        :return: ID, memo, tags
        """
        if not notes and not filter_key:
            notes = self.notebook.Notes
        elif not notes and filter_key:
            print("No Notes can be found with the keyword provided")

        for note in notes:
            print("{}: {}/{}".format(note.id, note.memo, note.tags))

    def search_notes(self):
        """
        Input search keyword from input
        Search for a user input keyword from the notes and associated tags
        :return: list of notes with the keyword
        """
        keyword = input("Enter a keyword to search: ")
        results = self.notebook.search(keyword)
        self.show_notes(results, True)

    def add_note(self):
        """
        adds note to an existing notebook
        :return: Add a note to notebook
        """
        memo = input("Enter the new note: ")
        self.notebook.new_note(memo)
        print("New Note has been added")

    def modify_note(self):
        """
        Modify note for a given note with an ID provided by the user
        :return: Modify note of a existing Notebook
        """
        note_id = input("Enter the note id: ")
        memo = input("Enter the modified note: ")
        self.notebook.modify_note(int(note_id), memo)
        print("Note {} is modified".format(note_id))

    def modify_tags(self):
        """
        Modify tags for a given note with an ID provided by the user
        :return: Modify tags of a existing Notebook
        """
        note_id = input("Enter the note id: ")
        tags = input("Enter the modified tag(s): ")
        self.notebook.modify_tag(int(note_id), tags)
        print("Tag {} is modified".format(note_id))

    @staticmethod
    def quit():
        print("Thank you for using the Notebook app")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
