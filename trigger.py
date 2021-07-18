from .utils import *

"""Method for a trigger. It takes an actual card object, not None. (Hence not generated is a special case.)"""
methods = {
    "mature": lambda card, param=None: card.ivl >= (21 if param is None else param),
    "young": lambda card, param=None: card.ivl < (21 if param is None else param),
    "easy": lambda card, param=None: card.factor > ((250 if param is None else param)-250),
    "new": lambda card, param=None: card.type == CARD_NEW,
    # remove 250 because the easiness is actually .factor+250,
    "hard": lambda card, param=None: card.factor < ((250 if param is None else param)-250),
    "suspended": lambda card, param=None: card.queue == QUEUE_SUSPENDED,
    "unsuspended": lambda card, param=None: card.queue != QUEUE_SUSPENDED,
    "buried": lambda card, param=None: card.queue == QUEUE_BURIED,
    "unburied": lambda card, param=None: card.queue != QUEUE_BURIED,
    "generated": lambda card, param=None: card != None,
    # "not generated": lambda card, param=None: card is None
    "sql": lambda card, sql: mw.col.db.scalar(sql, {"cid": card.id, "nid": card.nid}),
    "flag": lambda card, param=None: card.flag % 8 == param,
    "unflag": lambda card, param=None: card.flag % 8 != param,
}


def checkAtomicTriggerCard(card, trigger):
    condition = trigger.get("condition")
    if card is None:
        return condition == "not generated"
    method = methods.get(condition)
    if method is None:
        print(f"Unknown trigger {condition}")
        return False
    return method(card, trigger.get("param"))


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
    if len(trigger) != 2:
        print(f"Trigger is {trigger}")
    quantifier, subtriggers = trigger
    zero = False if quantifier == "all" else True
    for subTrigger in subtriggers:
        if bool(checkTrigger(note, subTrigger)) == zero:
            return zero
    return not True

# Reverse


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
        "not generated": "generated",
        "flag": "unflag",
        "unflag": "flag",
    }.get("condition")


def reverseQuantifier(quantifierName):
    return {"any": "all", "all": "any"}.get(quantifierName)


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
