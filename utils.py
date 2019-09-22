from .consts import *
from aqt import mw

def getTemplate(model, cardName):
    for tmpl in model["tmpls"]:
        if tmpl['name'] == cardName:
            return tmpl
    print(f"""No card type "{cardName}" in {model['name']}""")
    return None

def getTemplateOrd(model, cardName):
    tmpl = getTemplate(model, cardName)
    if tmpl == None:
        return None
    return tmpl['ord']
                  
def getCardId(note, cardName):
    ord = getTemplateOrd(note.model(), cardName)
    if ord == None:
        return None
    return mw.col.db.scalar("select id from cards where nid = ? and ord = ?", note.id, ord)

def getCard(note, cardName):
    cid = getCardId(note, cardName)
    if cid is None:
        return None
    return mw.col.getCard(cid)

