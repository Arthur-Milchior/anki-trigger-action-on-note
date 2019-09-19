from anki.hooks import addHook
from .rule import updateNid
from aqt import mw
from .config import getUserOption

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from anki.lang import _
from aqt.utils import tooltip

def setupMenu(browser):
    a = QAction(_("Apply rules to note"), browser)
    shortcut = getUserOption("Shortcut: Apply rules","Ctrl+alt+Shift+R")
    if shortcut:
        a.setShortcut(QKeySequence(shortcut))
    a.triggered.connect(lambda : onApply(browser))
    browser.form.menuEdit.addAction(a)

def onApply(browser):
    mw.checkpoint("Apply rules")
    mw.progress.start()
    nbChange = 0
    for nid in browser.selectedNotes():
        if updateNid(nid):
            nbChange += 1
        mw.progress.finish()
    if nbChange:
        mw.reset()
        tooltip(_("%d note(s) changed")% nbChange)
    else:
        tooltip("No change")

addHook("browser.setupMenus", setupMenu)
