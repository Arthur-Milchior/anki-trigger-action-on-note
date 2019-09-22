from anki.hooks import addHook
from rule import updateAll
from aqt.qt import QAction
from aqt import mw

addHook()

action = QAction(aqt.mw)
action.setText("Apply trigger->action rules")
mw.form.menuTools.addAction(action)
action.triggered.connect(updateAll)
