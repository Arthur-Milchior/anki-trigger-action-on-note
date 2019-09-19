from anki.hooks import addHook

from .rule import updateNid

nid = 1537365750042
addHook("profileLoaded", lambda: print("sent") or updateNid(nid))
