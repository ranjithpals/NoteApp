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

    def find_note(self, note_id):
        """
        Find the ID of the Note within the Notebook
        :param note_id:
        :return: Integer
        """
        for note in self.Notes:
            if note.id == note_id:
                return note
        return None

    def modify_note(self, note_id, memo):
        """
        Modify an exiting note in a Notebook
        :param note_id:
        :param memo:
        :return: Boolean (Note is modified or NOT)
        """
        note = self.find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False

    def modify_tag(self, note_id, str_tags):
        """
        Modify the tags associated with an existing Note in a Notebook
        :param note_id:
        :param str_tags:
        :return: Boolean (Note tag is modified or NOT)
        """
        note = self.find_note(note_id)
        if note:
            note.tags = str_tags
            return True
        else:
            return False

    def search(self, keyword):
        """
        Search if the keyword exists in Notebook and list the memos containing the Keywords
        :param keyword:
        :return: list of notes matching the user provided keyword
        """
        return [note for note in self.Notes if note.match(keyword)]


