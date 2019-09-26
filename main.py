from anki.hooks import addHook
from aqt import mw
from aqt.qt import QAction

from .rule import updateAll

action = QAction(mw)
action.setText("Apply trigger->action rules")
mw.form.menuTools.addAction(action)
action.triggered.connect(updateAll)
