# UFO-invasion
Adaption (attempted?) of "Python Crash Course" chapter 12 to be horizontal shmup

## Here's a loose list of steps 
 - 1st step: just get the player ship up on a screen - **completed**
 - 2nd step: moving ship up/down constrained by top and bottom of window - **completed**
 - 3rd step: firing bullet across screen - **completed** ```(bullets don't delete themselves yet)```
 - 4th step: placing 1 column of aliens on screen at opposite end of window via while loop - **completed** `I even did this in a while loop using a separate method call. `
 - 5th step: draw multiple columns of aliens via embedded while loops **completed**
   - make columns move incrementally to the left towards player **completed**
 - 6th step: bullets collide with aliens, elminating each one **completed**
 - 7th step: scoring system, tracking number of tries/game restarts left **completed**
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

Today I did something of a speedrun through chapter 14. I mean it took about 3 hours total but compared to the prior two chapters it was very quick.

I've made my unnecessary back up copies of the scripts so now I can go in and take out redundant code and remove large chunk of the comments taking up so much space in the editing window.

Then I'll have to figure out what enhancement I want to do next. A title screen and pushing a key for pause would be the most obvious. Alongside a settings menu and if nothing else being able to choose between controls (arrow keys versus AWSD).

I have a lot of ideas but relatively little on the part where I know how to implement them and in what order. I know sound/music would come in eventually for instance but at this moment I don't know how to implement that.

Part of me wants to use this version of the reference and start over from scratch implementing things like menus and music from a much earlier phase.

First though I'll probably do some experimenting with pygame like writing shapes to the screen and seeing if i can get user input to show up as its typed on the screen. I may just use the all-purpose "really had to python" repository for that if anybody cared enough to follow.



---


## Old news


I've officially reached the end of chapter 13. This means The only thing left include things like buttons for the pause menu, the pause functionality, a Title screen with a start button, tracking the player score and high scores and resetting upon player losing all lives. Still necessary to be a "real" game but as it plays now it is technically a "game".

Speaking of which, right now bullets travel all the way through any/all aliens they collide with and I've made the bullets commically large as part of troubleshooting.

So the game is sideways alien invaders: the player fires bullets at the alien fleet, the fleet moves on the screen that to the left and upwards the over and down again. This fleet doesn't increase in speed and there's no score tracking nor lives tracked.

There's an extreme amount of unnecessary comments right now so if you wanted to change the bullet setting you could.

I did re-re-realize that settings had to be changed via manually editing the JSON file at the moment as I wanted that to be the definitive place for the settings. Since there's no edit-back-to-settings.py functionality, as long as that JSON exists that is what it will do.

I've actually started a "project" through github associated with this repo. I have no idea if it's publically accessible or how to share it though. 

I'm planning more enhancements once I get through chapter 14.


---




After many, many more iterations and I don't know how many hours of work I managed to get a column aliens to ship as the "fleet". This was done with the fleet and create alien methods. I was still using an invisible spawned alien for the task though.

Then, I worked on creating multiple columns of aliens with a second while loop. I arbitrarily decided to make the columns of aliens take up two-thirds of the game window, resulting in more aliens on screen than the book version of the game. Since I put in an "alien tracker" variable to count how many aliens I have total I might have to limit the total number of columns to not make this game too over the top with the effing aliens.

Long story short I managed to spawn mutliple columns of aliens using the top/left predefined variables of the alien objects along witht he top/bottom of the screen. 

After doing this, I found a [youtube video with this same functionality](https://youtu.be/mqz1_wRSMwo?si=6cMv9G3c1mD_6JAI&t=404) but accomplished in a much easier and straightforward sort of a way. Which is kind of infuriating. Part of me wants to just switch from while loops to for loops now, like in the video. But this would make re-following the book that much difficult. Also the video uses a sprite sheet, which looked like a much better approach to me.

So to summarize the approach I have right now to spawning the fleet of aliens: create an instance of an Alien and set its x and y coordinates. 

Then, using those coordinates as a reference point, start spawning a column aliens. When the right of one alien gets too close to the bottom of the window adjust the x coordinate and spawn a new column.

Keep making columns until x is 2/3 or so of the screen from the right. 

I was trying to figure out how to do this without spawning the initial invisible alien but ended up just falling back to this way. Before I saw the video. 

---

I was working on the while loop to draw in the fleet of aliens and now I think I understand a lot more how the whole algo for doing that works.

I actually took a little different approach. At least that's what I'm telling myself.

I create a new variable in the settings file called ```self.fleet_ship_spacing``` and set it to an integer value. Then I use that in conjuction with the height of the alien ship relative to the "bottom" of the prior ship as a way to add in consistently space the alien ships apart vertically. Okay I don't if that was obvious to tell what I was talking about or not but I'm going with it.

I still have to convert this all into a while loop and make sure it doesn't go off the bottom of the screen.

This is still in a very still-in-development sort of a state at the moment, but at least I can see noticable progress. Must be all those excercises and puzzles I've been doing.

Actually, unless I'm misunderstanding (which is possible) the Crash Course book is approaching this coordinates of the fleet ships thing kind of oddly.


---

It occured to me I should probably describe in more detail what I did with the fleet code so far, _before_ I start changing it with a while loop.

I went through multiple iterations of trying to figure this out. The last time I had attempted this re-write-as-horizontal I was having an issue with an extra alien showing up unaligned with the aliens associated with the fleet and I couldn't figure out why that was.

This time I think I did figure this out: firstly the alien images/objects are added to this group via a method with pygame, like this:

```Python
self.aliensGroup.add(new_alien, sec_alien, third_alien)
```

 The group is then sent to this pygame draw method, lke this:

```Python
self.aliensGroup.draw(self.screen)
```

So in the first attempt I must have been inadvertently also sending the the initially created alien object to the group as well as the generated or "spawned" aliens created in the while loop.

Realizing this in this attempt, I created an alien but didn't add it to the group. Then I created 3 more aliens I added to the alien group invidually which were then subsequently drawn to the screen.

After more experimenting I was using the top of the screen and heights of the alien image to try and space the different aliens apart from each other.

That's when I realized I use the predefined variables provided by pygame for the top/bottom/etc part of the images. 

I should note here there are both the literal PNG images I am referring to as well as the assocated rectangles with each image. I only somewhat know why this image-rectangle relationship is required. Probably because a lot of these methods and pre-defined variables are only available to rectangles. That's just a minor detail in case I inadvertently refer to the rectangle of the alien etc.

As it stands now in the code - pre-while-loop - I'm putting up 3 alien for the fleet all perfect aligned vertically and spaced from each other.

Here is the snippet to hopefully help demonstrate the point. I'm not saying this is the right way of doing it. Just that I managed to get it to work this way. Next step while-loop.


```Python

  alien = Alien(self) # Never added to group/draw to screen. It's a magic/invisible alien...
  alien_height = alien.rect.height # This establishes the height of the magic alien
  
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

---

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

---

I've been copy/pasting these pre-defines into various class files (alien.py and ship.py for instance). These are accessible via rectangles. So rectangles are created from image dimensions. Or image coordinates are defined via image rectangle dimensions. Different combinations of those things. The point is these are convenient.


```
This should probably universal reference at this point

The Rect object has several virtual attributes which can be used to move and align the Rect:
x,y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
w,h


All of these attributes can be assigned to: 
rect1.right = 10
rect2.center = (20,30)
```

