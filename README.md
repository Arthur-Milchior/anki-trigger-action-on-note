# Relate cards of a note
## Rationale
I'm using anki to practice more and more complicated things. I'm going
to give an example to illustrate the problem this add-on solves.

I play piano. I want to practice scales. I have a note type for
scales, with cards such as «left hand one octave», «right hand one
octave», «both hands one octave», and then the same things for two
octaves.

When I can play «both hands two octaves» easily, there is no reason to
practice a single hand/octave. Thus, I want that, when the more
complex card is mature, the less complex ones are suspended.  However,
if suddenly I can't play two octaves two hand easily, so that this card
becomes young because I pressed «again», then I want to unsuspend the
other cards, in order to practice them again.

I don't want to see «two octaves two hands» until all of the other
cards are mature. So I have a rule stating that this card is suspended
by default, and unsuspended when all other cards are mature.

In fact, most of the time, «one hand one octave» is too easy. So I want
to suspend it by default, and unsuspend it only if I suspended either 
«both hands one octave» or «one hand two octaves».

I usually play two octaves. The only
time where I want to play a single octave is when I decided to suspend
the two octaves cards because they are too hard. So I want to have a
rule which states that, by default, one octave one hand is suspended,
and that it's unsuspended only if two octaves one hand is suspended.

This add-on allows you to do all of that, and even more.

## Usage
Once you have created rules, you can apply them by selecting notes in
the browser, and clicking on `Edit>Apply trigger->action rules`.

You can also apply it to all notes, from the main window, by doing
`Tools>Apply trigger->action rules`

Anki will ask you whether you want to automatically apply rules the
first time a rule may potentially be applied. Beware, if you had
created a buggy rule, then you'll automatically apply bugs. However,
nothing should be irreparable (that's why I didn't create a "delete"
rule). If you want to change this setting, you can simply change
the add-on configuration.

## Examples
I've been told this add-on needs examples. So here are two real life
examples from my collection. These are still works in progress, and
I'll probably make them more complete when I see the need for it.

You should probably install add-on
[112201952](https://ankiweb.net/shared/info/112201952) to read the
examples, because it'll allow you to see the configuration in a
readable way.

My card types are big, so you may want to use add-on
[777545149](https://ankiweb.net/shared/info/777545149) to make Anki
quicker before taking a look at them in details.

### Two languages

Let's assume that you want to learn German and use "[4000 German Words by Frequency](https://ankiweb.net/shared/info/653061995)". Each note has two
cards: "German -> English" and "English -> German". If you're like me,
the first card is much easier than the second one. So maybe you want to wait until the first card is mature to show the second. In this case, you'd use [these rules](example_german.json).

There are two rules. If English -> German is new or young, then German -> English should be suspended. This is what occurs when the deck is added to your collection. The second rule is that when English -> German is mature, then German -> English should be unsuspended. 

### Songs
I want to learn a song stanza by stanza, unless it's
too difficult, in which case I want to learn line by line.

So this [song deck](example_song.apkg) has a note type where each
card asks me for a stanza. If the stanza becomes mature, then Anki will
suspend the cards related to lines. If I find that the stanza cards
are too complicated, I suspend them; in this case Anki will show me
the lines. In the future, I'll also make a rule stating that when I
know all lines, the stanza card should be unsuspended. 

Here is the long [add-on configuration](example_song.json) for this
example. Currently, it only contains rules which state that when some
card is mature, other cards should be suspended. Please add the song
deck to your collection while reading the configuration, otherwise it
will makes no sense.

### Piano scale
This example is similar. I want to learn scales on piano. When I know
how to play two octaves, I want to suspend the cards asking me to play
one octave. When I know how to play two hands, I want to suspend the
cards asking me to play one hand. Here are the [example deck](example_piano.apkg) and its [configuration](example_piano.json)

I'll explain one line.
```json
{"trigger": {"condition": "mature", "cards": "/\"}, "action": {"action": "suspend", "cards": ["\", "/", "right/\", "right\", "right/", "left/\", "left\", "left/"]}},
```
The card "/\" is the card asking me to play one octave increasing and then one octave decreasing with both hands. When I know how to do that correctly, I want to suspend all of the cards listed at the end. That is:
* "\", which asks me to play an octave decreasing with both hands
* "/", which asks me to play an octave increasing with both hands
* "right/\" which asks me to play the octave both ways with the right hand
* etc.

Note that \, /, right\, right/, are the names of my card types; they have nothing to do with the add-on. They are here only because the name in the configuration must be the same name as those in your collection. Here my collection has a note type whose name is "Piano scale" and which has cards named "/\", "\", "/", "right/\", "right\", "right/", "left/\", "left\", "left/" and so on.

(For technical reason, each time I use \, I should actually write two \\. So the real line in the example is:
```json
{"trigger": {"condition": "mature", "cards": "/\\"}, "action": {"action": "suspend", "cards": ["\\", "/", "right/\\", "right\\", "right/", "left/\\", "left\\", "left/"]}},
```
)
## Warning
### Clozes
Currently, this add-on does not work for note types with cloze deletion. It should give an error message if you try to use it on such notes. It may change in the future; however it's not clear to me what would be the point of this add-on since cloze numbers are arbitrary.

### Computer only
This add-on can only affect cards on computers where the add-on is
installed. That means that if you review cards on IOS, ankiweb,
ankidroid.... you need to sync with your computer in order to apply
the rules.

### It's easy to make an error
This add-on may (un)suspend or (un)bury a lot of cards. This may make
your life complicated if you enter the wrong set of rules. So make a
backup and test your rule well.

### Order of rules
Rules are applied in the order in which they are listed. You should
take this into consideration. Indeed, one rule application may trigger
the condition for another rule application. This second rule will be
applied either:
* immediately if it is after the first rule in the list
* at some random time in the future otherwise, when this add-on checks
  again for rules to apply.

In fact, you could even create contradictory rules, such as «When card
A is suspended, suspend B. When B is suspended, unsuspend A. When A is
unsuspended, unsuspend B. When B is unsuspended, suspend A». You are
responsible to avoid such silly rules yourself.

## Configuration
By default, there is an example configuration. However, it's not a
real configuration. Indeed, if I created a real configuration, it
would apply rules to your collection and change it in a way you don't
want.

Read [config](config.md) to know more about the configuration.

## Technical
## Internal
## Version 2.0
None

## TODO
Ensure that actions occur every time change may occur, i.e. at least:
* review in Anki
* sync
* full sync
* import

* Allow rules to apply to cloze

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-
Addon number| [1981494159](https://ankiweb.net/shared/info/1981494159)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
