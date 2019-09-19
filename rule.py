from .trigger import checkTrigger, reverseTrigger
from .action import applyActions, reverseAction
from .config import getUserOption
from aqt import mw

def applyRuleToNote(note, rule):
    """Whether there was a change"""
    if rule is None:
        return False
    print(f"Applying rule {rule}")
    if not checkTrigger(note, rule["trigger"]):
        print("trigger failed to apply")
        return False
    print("Trigger succeeded")
    ret = applyActions(note, rule["action"])
    if ret:
        print("Some change")
    else:
        print("no change")
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
        iter +=1
        if iter >= 10:
            print(f"There was more than 10 application of the rules to note {note.id}, something is probably wrong. Aborting.")
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
            
    
