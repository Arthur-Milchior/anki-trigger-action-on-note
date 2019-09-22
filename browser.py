from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from anki.hooks import addHook
from anki.lang import _
from aqt import mw
from aqt.utils import showWarning, tooltip

from .config import getUserOption
from .rule import updateNid


def setupMenu(browser):
    a = QAction(_("Apply rules to note"), browser)
    shortcut = getUserOption("Shortcut: Apply rules", "Ctrl+alt+Shift+R")
    if shortcut:
        a.setShortcut(QKeySequence(shortcut))
    a.triggered.connect(lambda: onApply(browser))
    browser.form.menuEdit.addAction(a)


def onApply(browser):
    mw.checkpoint("Apply rules")
    mw.progress.start()
    nbChange = 0
    missingNoteTypes = set()
    for nid in browser.selectedNotes():
        nbChangeNid, missingNid = updateNid(nid)
        if nbChangeNid:
            nbChange += 1
        missingNoteTypes |= missingNid
    mw.progress.finish()
    if nbChange:
        mw.reset()
        tooltip(_("%d note(s) changed") % nbChange)
    else:
        tooltip("No change")
    if missingNoteTypes:
        showWarning(_("You asked to apply rules to notes whose types are %s. There are no rules for those note type(s). Please check your add-on configuration.") % str(missingNoteTypes))


addHook("browser.setupMenus", setupMenu)
