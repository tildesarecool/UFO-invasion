# UFO-invasion
Adaption (attempted?) of "Python Crash Course" chapter 12 to be horizontal shmup

## Here's a loose list of steps 
 - 1st step: just get the player ship up on a screen - completed
 - 2nd step: moving ship up/down constrained by top and bottom of window - completed 
 - 3rd step: firing bullet across screen - completed (bullets don't delete themselves yet)
 - 4th step: placing 1 column of aliens on screen at opposite end of window via while loop - (alies show up, while loop pending)
 - 5th step: draw multiple columns of aliens via embedded while loops
 - 6th step: bullets collide with aliens, elminating each one
 - 7th step: scoring system, tracking number of tries/game restarts left
 - 8th step: a "click to play" button/pause button

Stretch/dream/at the end goals:
- music, sound effects
- save settings to JSON file/load settings from JSON file
 **complete:** ```much more straight forward to implement than I thought. Keep in mind I haven't fully tested all "edge cases" around this feature.```
  - a settings menu in-game where things like sound volume and resolution could be set
  - a "secret" debug input box i can access to change setting values while playing
- at least two different varieties of enemies
  - one or all enemies fly in patterns instead of move down/move up/move closer
  - enemies fire bullets back at random

## The Good, Bad and/or Newest news

I was working on the while loop to draw in the fleet of aliens and now I think I understand
a lot more how the whole algo for doing that works.

I actually took a little different approach. At least that's what I'm telling myself.

I create a new variable in the settings file called ```self.fleet_ship_spacing``` and set it to an integer value. Then I use that in conjuction with the height of the alien ship relative to the "bottom" of the prior ship as a way to add in consistently space the alien ships apart vertically. Okay I don't if that was obvious to tell what I was talking about or not but I'm going with it.

I still have to convert this all into a while loop and make sure it doesn't go off the bottom of the screen.

This is still in a very still-in-development sort of a state at the moment, but at least I can see noticable progress. Must be all those excercises and puzzles I've been doing.

Actually, unless I'm misunderstanding (which is possible) the Crash Course book is approaching this coordinates of the fleet ships thing kind of oddly.


## Old news
The script actually runs now. Took me a while to even get that far.

Bad news though i can't control the ship any more, the bullets don't fire and the fleet start at the top and moves down instead of at the right and move left. 

The fleet does move though.

So it's just a matter of figuring out some x/y swapping and further debugging.

I'll perhaps work on this tomorrow

Side note: apparently the multi-line python comment method starting/ending with triple quotes 
'''
actually has to be properly indented.
I thought it was just a multi-line comment like the
/* */ 
used in some many other languages. 
Improper indenting of those quotes results in the script not running. Took me a long time to learn that the hard way.