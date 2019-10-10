from anki.collection import _Collection
from anki.lang import _
from aqt.utils import askUser

from .config import getUserOption, setUserOption
from .rule import updateAll


def auto():
    aut = getUserOption("Apply on save", None)
    if aut is None:
        aut = askUser(_("""Anki is saving right now. Do you want the add-on "Trigger and actions"(1981494159) to trigger all rules while saving ?
You can change your choice in the add-on configuration later. 
See https://github.com/Arthur-Milchior/anki-trigger-action-on-note for more details."""), defaultno=True)
        setUserOption("Apply on save", aut)
    return aut


oldSave = _Collection.save


def save(self, *args, **kwargs):
    if auto():
        updateAll()
    oldSave(self, *args, **kwargs)
