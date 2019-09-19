from .utils import *


def unburyCard(card):
    if card.queue in ({QUEUE_USER_BURIED}, {QUEUE_SCHED_BURIED}):
        card.queue = card.type
        card.flush()
        return True
    return False


def buryCard(card):
    if card.queue not in ({QUEUE_USER_BURIED}, {QUEUE_SCHED_BURIED}):
        card.queue = QUEUE_USER_BURIED
        card.flush()
        return True
    return False


def unsuspendCard(card):
    if card.queue == QUEUE_SUSPENDED:
        card.queue = card.type
        card.flush()
        return True
    return False


def suspendCard(card):
    if card.queue != QUEUE_SUSPENDED:
        card.queue = QUEUE_SUSPENDED
        card.flush()
        return True
    return False


actionMethods = {
    "suspend": suspendCard,
    "unsuspend": unsuspendCard,
    "bury": buryCard,
    "unbury": unburyCard,
}


def applyActionToCard(card, method):
    if card is not None:
        return method(card)
    return False


def applyActionToNote(note, action):
    actionName = action.get("action")
    method = actionMethods.get(actionName)
    if method is None:
        return
    cardTypes = action["cards"]
    if isinstance(cardTypes, str):
        cardTypes = [cardTypes]
    someChange = False
    for cardName in cardTypes:
        card = getCard(note, cardName)
        someChange = applyActionToCard(card, method) or someChange
    return someChange


def applyActions(note, actions):
    someChange = False
    if isinstance(actions, dict):
        actions = [actions]
    for action in actions:
        if applyActionToNote(note, action):
            someChange = True
    return someChange

# Reverse


def reverseActionName(actionName):
    if actionName.startswith("un"):
        return actionName[2:]
    return f"un{actionName}"


def reverseAtomicAction(action):
    return {
        **action,
        "action": reverseActionName(action["action"])
    }


def reverseAction(actions):
    if isinstance(actions, list):
        actions = [actions]
    return [reverseAtomicAction(atomicAction) for atomicAction in actions]
