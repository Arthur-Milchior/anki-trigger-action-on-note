The configuration contains a simple entry: "rules". A rule is simply a
dictionnary associating to each note type name a "note type rule".

A "note type rule" itself is a list of "atomic rule".

An "atomic rule" can take the following parameter:
* "trigger": a trigger.
* "action": an action
* "autoReverse": if set to true, the inverse of the action will be
  applied when the triggering rules does not hold anymore.
  
A trigger is either:
* an atomic trigger/action
* a tuple with:
** "any" or "all"
** a list of trigger

The non-atomic trigger holds if any/all atomic triggers holds.

An "atomic trigger" is:
* "condition": a condition which must be satisfied. It can be
  "mature", "young", "suspended", "unsuspended", "buried", "unburied",
  "easy", "hard", "generated", "not generated", "flag", "unflag", "new" or
  expressed as a sql request where `:cid` is the card id and `:nid` is
  note id. The query should return a boolean scalar.
* "param": the value at which a card is supposed to be
  mature/easy or The number of the flag. By default a card is mature when it's interval is 21
  days and an easy card is one whose ease it's at least 300%
* "card types: a (list of) card type's name on which this trigger apply. If
  some card does not exists, the trigger fails (unless the condition
  is "not generated")

A action is either:
* an atomic action
* a list of atomic action

An atomic action is:
* "action": what to do to other cards, when the triggering rules
  apply. Actions are "suspend", "unsuspend", "bury", "unbury", "flagi"
  with "i" a flag number between 0 and 4 included.
* "card types: a list of card type on which this action apply. If some
  card does not exists, the action is not applied to it simply.

