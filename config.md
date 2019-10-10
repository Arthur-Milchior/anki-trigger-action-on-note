The configuration contains a simple entry: "rules". A rule is simply a
dictionary associating to each note type name a "note type rule".

A "note type rule" itself is a list of "atomic rules".

An "atomic rule" can take the following parameters:
* "trigger": a trigger.
* "action": an action
* "autoReverse": if set to true, the inverse of the action will be
  applied when the triggering rule does not hold anymore.

A trigger is either:
* an atomic trigger/action
* a tuple with:
** "any" or "all"
** a list of triggers

The non-atomic trigger holds if any/all atomic triggers hold.

An "atomic trigger" is:
* "condition": A condition which must be satisfied. It can be
  "mature", "young", "suspended", "unsuspended", "buried", "unburied",
  "easy", "hard", "generated", "not generated", "flag", "unflag", "new" or
  expressed as a sql request where `:cid` is the card id and `:nid` is
  note id. The query should return a boolean scalar.
* "param": The value at which a card is supposed to be
  mature/easy, or the number of the flag. By default a card is mature when its interval is 21
  days and an easy card is one whose ease is at least 300%
* "card types": A card type name or list of names to which this trigger applies. If
  no card of that type exists, the trigger fails (unless the condition is "not generated")

An action is either:
* an atomic action
* a list of atomic actions

An atomic action is:
* "action": what to do to other cards when the triggering rules
  apply. Actions are "suspend", "unsuspend", "bury", "unbury", "flagN"
  (where "N" is a flag number between 0 and 4).
* "card types: a list of card types on which this action applies. If no
  card of that type exists, the action has no effect.

