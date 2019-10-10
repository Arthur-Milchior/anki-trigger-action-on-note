from .trigger import checkTrigger, reverseTrigger
from .action import applyActions, reverseAction
from .config import getUserOption
from aqt import mw

"""True when applying holds. This ensure that a flush triggered by application of the rules does not trigger other rule application"""
currentlyApplying = False

def applyRuleToNote(note, rule):
    """Whether there was a change"""
    global currentlyApplying
    if currentlyApplying:
        return
    currentlyApplying = True
    if rule is None:
        return False
    #print(f"Applying rule {rule}")
    if not checkTrigger(note, rule["trigger"]):
        #print("trigger failed to apply")
        return False
    #print("Trigger succeeded")
    ret = applyActions(note, rule["action"])
    # if ret:
    #     #print("Some change")
    # else:
    #     #print("no change")
    currentlyApplying = False
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
    if rules is None:
        return 0, {modelName}
    iter = 0
    while applyRulesToNote(note, rules):
        iter +=1
        if iter >= 10:
            #print(f"There was more than 10 application of the rules to note {note.id}, something is probably wrong. Aborting.")
            break
    return iter, set()
        

def updateNid(nid):
    note = mw.col.getNote(nid)
    return updateNote(note)

def updateAll():
    nbChanges = 0
    missings = set()
    for nid in mw.col.findNotes(""):
        nbChangeNid, missingNid = updateNid(nid)
        nbChanges +=  nbChangeNid
        missings |= missingNid
    return nbChanges, missings
            
    
