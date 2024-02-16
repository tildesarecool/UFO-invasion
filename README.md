# UFO-invasion
Adaption (attempted?) of "Python Crash Course" chapter 12 to be horizontal shmup

## Here's a loose list of steps 
 - 1st step: just get the player ship up on a screen - **completed**
 - 2nd step: moving ship up/down constrained by top and bottom of window - **completed**
 - 3rd step: firing bullet across screen - **completed** ```(bullets don't delete themselves yet)```
 - 4th step: placing 1 column of aliens on screen at opposite end of window via while loop - (aliens show up, while loop pending)
 - 5th step: draw multiple columns of aliens via embedded while loops
 - 6th step: bullets collide with aliens, elminating each one
 - 7th step: scoring system, tracking number of tries/game restarts left
 - 8th step: a "click to play" button/pause button

Stretch/dream/at the end goals:
- music, sound effects
- save settings to JSON file/load settings from JSON file
 **complete:** ```Just when I thought I was done I ended up pretty much re-writing it. But it seems to be working as I intended now (pending additional testing).```
  - a settings menu in-game where things like sound volume and resolution could be set
  - a "secret" debug input box I can access to change setting values while playing
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

---

It occured to me I should probably describe in more detail what I did with the fleet code so far, _before_ I start changing it with a while loop.

I went through multiple iterations of trying to figure this out. The last time I had attempted this re-write-as-horizontal I as having an issue with an extra alien showing up unaligned with the aliens associated with the fleet and I couldn't figure out why that was.

This time I think I did figure this out: firstly the alien images/objects are added to this group via a method with pygame, like this:

```Python
self.aliensGroup.add(new_alien, sec_alien, third_alien)
```

 The group is then sent to this pygame draw method, lke this:

```Python
self.aliensGroup.draw(self.screen)
```

So in the first attempt I must have been inadvertently also sending the the initially created alien boject to the group as well as the generated or "spawned" aliens created in the while loop.

Realizing this in this attempt, I created an alien but didn't add it to the group. Then I created 3 more aliens I added to the alien group invidually which were then subsequently drawn to the screen.

After more experimenting I was using the top of the screen and heights of the alien image to try and space the different aliens apart from each other.

That's when I realized I use the predefined variables provided by pygame for the top/bottom/etc part of the images. 

I should note here there are both the literal PNG images I referring to as well as the assocated rectangles with each image. I only somewhat know why this image-rectangle relationship is required. Probably because a lot of these methods and pre-defined variables are only available to rectangles. That's just a minor detail in case I inadvertently refer to the rectangle of the alien etc.

As it stands now in the code - pre-while-loop - I'm putting up 3 alien for the fleet all perfect aligned vertically and spaced from each other.

Here is the snippet to hopefully help demonstrate the point. I'm not saying this is the right way of doing it. Just that I managed to get it to work this way. Next step while-loop.


```Python

  alien = Alien(self) # Never added to group/draw to screen. It's a magic/invisible alien...
  alien_height = alien.rect.height # This establishes the height of the magic alien
  alien_fleet_spacing = alien.rect.height * 2 # initial spacing, probably not needed
  
  # I recreated the self.settings.fleet_ship_spacing as a variable in settings.py
  # so i could easily adjust it like everything else - note: 10px might be too much
  # in alien.py is the line
  # self.y = float(self.rect.y)
  # does this seem convuluted? Nahh
  # this is saying "taken y coord of invisible alien and subtract ship spacing value
  # setting from it - then set that to "current_y" coord
  current_y = alien.y - self.settings.fleet_ship_spacing  # settings.py based spacing
  
  # create threw aliens for the alien fleet
  new_alien = Alien(self)
  sec_alien = Alien(self)
  third_alien = Alien(self)
  
  # first alien of fleet can just use current_y
  new_alien.y = current_y 
  new_alien.rect.y = current_y 
  
  # alien 2 of fleet just use the "bottom" of the first visiable alien
  # and add the spacing found in settings.py. 
  # so space between the bottom of the first alien and top of the next alien
  # is that fleet-ship-spacing value...
  
  sec_alien.y = new_alien.rect.bottom + self.settings.fleet_ship_spacing 
  
  # and rectangle for that alien is same
  sec_alien.rect.y = new_alien.rect.bottom + self.settings.fleet_ship_spacing  # 
  
  # for third alien do the same thing relative to the 2nd alien...and same for rectangle
  third_alien.y = sec_alien.rect.bottom + self.settings.fleet_ship_spacing 
  third_alien.rect.y = sec_alien.rect.bottom + self.settings.fleet_ship_spacing 
  
  # add all the aliens to the group for drawing to the screen
  self.aliensGroup.add(new_alien, sec_alien, third_alien)

```

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