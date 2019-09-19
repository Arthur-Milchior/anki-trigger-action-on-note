from aqt import mw

from .action import applyActions, reverseAction
from .config import getUserOption
from .trigger import checkTrigger, reverseTrigger


def applyRuleToNote(note, rule):
    """Whether there was a change"""
    if rule is None:
        return False
    if not checkTrigger(note, rule["trigger"]):
        return False
    ret = applyActions(note, rule["action"])
    return ret


def applyRulesToNote(note, rules):
    """Whether there was a change"""
    someChange = False
    for rule in rules:
        someChange = applyRuleToNote(note, rule) or someChange
    return someChange


def reverse(rule):
    return {**rule,
            "trigger": reverseTrigger(rule["trigger"]),
            "action": reverseAction(rule["action"]),
            }


def updateNote(note):
    model = note.model()
    modelName = model["name"]
    rules = getUserOption("rules").get(modelName)
    iter = 0
    while applyRulesToNote(note, rules):
        iter += 1
        if iter >= 10:
            break
    return iter


def updateNid(nid):
    note = mw.col.getNote(nid)
    return updateNote(note)


def updateAll():
    someChange = False
    for nid in mw.col.findNotes(""):
        someChange = updateNid(nid) or someChange
    return someChange
