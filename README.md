# Relate cards of a note
## Rationale
I'm using anki to practice more and more complicated things. I'm going
to take an example to illustrate the problem this add-on solves.

I play piano. I want to practice scales. I have a note type for
scales, with cards such as «left hand one octave», «right hand one
octave», «both hands one octave», and then the same things for two
octaves.

When I can play «both hands two octaves» easily, there is no reason to
practice a single hand/octave. Thus, I want that, when the more
complex card is mature, the less complex ones are suspended.  However,
if suddenly, I can't play two octaves two hand easily, that this card
becomes young because I pressed «again», then I want to unsuspend the
other cards, in order to practice them again.

I don't want to see «two octaves two hands» until all of the other
cards are mature. So I have a rule stating that this card is suspended
by default, and unsuspended when all other cards are mature.

In fact, most of the time, one hand one octave is too easy. So I want
to suspend it by default, and unsuspend it only if I suspended either

I cand directly play two octaves. The only
time where I want to play a single octave is when I decided to suspend
the two octaves cards because they are two hards. So I want to have a
rule which state that, by default, one octave one hand is suspended,
and that it's unsuspended only if two octaves one hand is suspended.

This add-on allow you to do all of that, and even more.

## Warning
### Computer only
This add-on can only affect cards on computers where the add-on is
installed. It means that if you see cards on IOS, ankiweb,
ankidroid.... you need to sync with your computer in order to apply
the rules.

### It's easy to make an error
This add-on may (un)suspend, (un)bury a lot of cards. This may makes
your life complicated if you did enter a wrong set of rules. So make a
back up and test your rule a lot before being sure that you want to
keep those rules alive.

### Order of rules
Rules are applied in the order if which they are listed. You should
take this in consideration. Indeed, one rule application may trigger
the condition for another rule application. This second rule will be
applied either:
* immediately if it is after the first rule in the list
* at some random time in the future otherwise, when this add-on check
  again for rules to apply.

In fact, you could even create contradictory rules. Such as «When card
A is suspended, suspend B. When B is suspended, unsuspend A. When A is
unsuspended, unsuspsend B. When B is unsuspended, suspend A». You are
responsible to avoid such silly rules yourself.

## Configuration
By default, there is an examples configuration. However, it's not a
real configuration. Indeed, if I created a real configuration, it
would apply rules to your collection and change it in a way you don't
want.

Read [config](config.md) to know more about the configuration.

## Technical
## Internal
## Version 2.0
None

## TODO
Ensure that actions occurs every time change may occur. I.e. at least:
* review in anki
* sync
* full sync
* import

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-
Addon number| [1981494159](https://ankiweb.net/shared/info/1981494159)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
