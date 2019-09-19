from .utils import *

methods = {
    "mature": lambda card, threshold=None: card.ivl>= (21 if threshold is None else threshold),
    "young": lambda card, threshold=None: card.ivl< (21 if threshold is None else threshold),
    "easy": lambda card, threshold=None: card.factor > ((250 if threshold is None else threshold)-250),
    #remove 250 because the easiness is actually .factor+250,
    "hard": lambda card, threshold=None: card.factor < ((250 if threshold is None else threshold)-250),
    "suspended": lambda card, threshold=None: card.queue == QUEUE_SUSPENDED,
    "unsuspended": lambda card, threshold=None: card.queue != QUEUE_SUSPENDED,
    "buried": lambda card, threshold=None: card.queue == QUEUE_BURIED,
    "unburied": lambda card, threshold=None: card.queue != QUEUE_BURIED,
    # "generated": lambda card, threshold=None: card != None
    # "not generated": lambda card, threshold=None: card == None
    "sql": lambda card, sql: mw.col.db.scalar(sql, {"cid": card.id, "nid": card.nid}),
}
    
def checkAtomicTriggerCard(card, trigger):
    condition = trigger.get("condition")
    if card is None:
        return condition == "not generated"
    method = methods.get(condition)
    if method is None:
        print(f"Unknown trigger {condition}")
        return False
    return method(card, trigger.get("threshold"))
    
def checkAtomicTriggerNote(note, trigger):
    cards = trigger["cards"]
    
    if isinstance(cards, str):
        cardName = cards
        return checkAtomicTriggerCard(getCard(note, cardName), trigger)
    quantifier, cards = cards
    zero = True if quantifier == "all" else False
    for cardName in cards:
        if checkAtomicTriggerCard(getCard(note, cardName), trigger) == zero:
            return zero
    return not zero

def checkTrigger(note, trigger):
    if isinstance(trigger, dict):
        return checkAtomicTriggerNote(note, trigger)
    quantifier, atomicTriggers = trigger
    zero = False if quantifier == "all" else True
    for subTrigger in trigger:
        if bool(checkTrigger(note, subTrigger)) == zero:
            return zero
    return not True

## Reverse
def reverseName(triggerName):
    return {
        "mature": "young",
        "young": "mature",
        "suspended": "unsuspended",
        "buried": "unburied",
        "easy": "hard",
        "generated": "not generated",
        "unsuspended": "suspended",
        "unburied": "buried",
        "hard": "easy",
        "not generated": "generated"
    }.get("condition")

def reverseQuantifier(quantifierName):
    return {"any":"all", "all":"any"}.get(quantifierName)

def reverseAtomicTrigger(atomicTrigger):
    condition = reverseName(atomicTrigger["condition"])
    if condition is None:
        return None
    return {
        **atomicTrigger,
        "condition": condition
    }

def reverseTrigger(trigger):
    quantifier, subTriggers = trigger
    return (
        reverseQuantifier(quantifier),
        [reverseTrigger(subTrigger) for subTrigger in subTriggers])
