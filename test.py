from .rule import updateNid
from anki.hooks import addHook
nid = 1537365750042
addHook("profileLoaded", lambda:print("sent") or updateNid(nid))
