import datetime as dt

# The ID number for the next created note
last_id = 0


class Note:
    """
    Class to handle the properties of Note
    + string Note
    + string Tags
    + Datetime CreateDate
    - match(str Keyword) -> Return Boolean
    """

    def __init__(self, memo, tags=''):
        """
        Create a note with a given text and tags set to empty string and creation datetime to current time.
        The ID is updated using a counter and assigned to the memo
        :param memo: the text added when note is created
        """
        self.memo = memo
        self.tags = tags
        self.createDate = dt.datetime.now()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, keyword):
        """
        Check if the keyword is found in the note
        :param keyword:
        :return: Boolean True/False
        """
        return keyword in self.memo or keyword in self.tags


class Notebook:
    """
    Class to create, manage notes within a Notebook, and modify tags, search notes
    """

    def __init__(self):
        """ Create a Notebook with empty list of notes """
        self.Notes = []

    def new_note(self, str_memo, str_tags=''):
        """
        Create a New Note using the Note object and add it to the Notebook (Notebook contains a list of Notes)
        :param str_memo:
        :param str_tags:
        :return:
        """
        self.Notes.append(Note(str_memo, str_tags))

    def modify_note(self, note_id, memo):
        """
        Modify an exiting note in a Notebook
        :param note_id:
        :param memo:
        :return:
        """
        for note in self.Notes:
            if note.id == note_id:
                note.memo = memo
                break
        else:
            print("Note ID does not exist, please provide another id")

    def modify_tag(self, note_id, str_tags):
        """
        Modify the tags associated with an existing Note in a Notebook
        :param note_id:
        :param str_tags:
        :return:
        """
        for note in self.Notes:
            if note.id == note_id:
                note.tags = str_tags
                break
        else:
            print("Note ID does not exist, please provide another id")

    def search(self, keyword):
        """
        Search if the keyword exists in Notebook and list the memos containing the Keywords
        :param keyword:
        :return:
        """

        return [note for note in self.Notes if note.match(keyword)]


