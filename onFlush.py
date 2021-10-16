from anki.cards import Card
from anki.lang import _
from anki.notes import Note
from aqt.utils import askUser

from .config import getUserOption, setUserOption
from .rule import updateNote


def auto():
    aut = getUserOption("Automatically applies rules", None)
    if aut is None:
        aut = askUser(_("""Do you want to automatically applies rules of the add-on "Trigger and actions"(1981494159) ? You can change your choice in the add-on configuration later. 
See https://github.com/Arthur-Milchior/anki-trigger-action-on-note for more details."""), defaultno=True)
        setUserOption("Automatically applies rules", aut)
    return aut


oldFlushCard = Card.flush


def flushCard(self):
    oldFlushCard(self)
    if auto():
        note = self.note()
        updateNote(note)


Card.flush = flushCard

oldFlushNote = Note.flush


def flushNote(self):
    oldFlushNote(self)
    if auto():
        updateNote(self)


Note.flush = flushNote
