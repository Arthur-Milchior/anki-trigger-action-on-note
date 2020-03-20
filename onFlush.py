from anki import hooks
from anki.lang import _
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


def flushCard(self):
    if auto():
        note = self.note()
        updateNote(note)


hooks.card_will_flush(flushCard)


def flushNote(self):
    if auto():
        updateNote(self)


hooks.note_will_flush(flushNote)
