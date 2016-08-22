#Code 201, Day 9 Learning Journal
###Thursday June 23nd, 2016

From the Git lecture this morning, I think most GITuations (but not all) can be avoided by just having a good workflow and keeping good git habits.  

I really enjoyed Brian's lecture from today, he does a good job of explaining what he's doing while he's doing it and moves right along at a brisk pace.  I built a pretty similar mock up of his template on my cookie site and will be putting some color into it tomorrow, along with whatever animations we end up doing.  Getting the text to sit in front of the banner was a challenge, it took me, Sam and finally Brian a while to untangle the absolute positioning (which was actually set right in the first place, we just couldn't figure out why it was sitting where it was).  

I also refactored some of the javascript, it's now a little simpler and uses the .push() method to move data into arrays.  I also kind of liked the this.varNameHere[i] = way to put data in there, but depending on your purpose either way seems to work.  The 'pushing into [i] slot makes more sense when you want to overwrite the data in the array without zeroing it out.  

I just sat on the couch and demo'd my site for my dad, he's pretty impressed with how far we've come in 9 days.  He has some programming background too so can understand quite a bit of the code.  Pretty spiffy so far, and now it's bed time.  


###Following the line break are my notes from the lecture.
---
Thursday June 23rd
Morning Notes

The schedule for today says “Advanced CSS Layout” but we’re really just on “brain detail” mopping up chunks of brains that are all over the floor (and everywhere else).  This is a review and catchup day, woo~

How git workflow changes when you’re working with forks and branches:

Alison = Navigator
Liz = Driver

Steps
- Make sure Alison’s repo is up to date and all changes are pushed to github.  
- Liz makes a fork of Alison’s master repo
- Liz clones her copy of Alison’s master repo down to her local machine to work on it
- Liz makes a new branch to work in
- Work happens
- ACP often in the new branch to Liz’s github

Once the work is back on github Liz can merge back into the master of her fork, then merge the forks back into Alison’s original work.  

I feel like I got a pretty good handle on this, git is a great state management tool and it’s just about understanding what you’re doing in which discreet location and keeping those things straight.  

Using:

git remote add upstream < url here>   <— this sets the connection up which lets us do a diagonal pull from Alison’s master to Liz’s master, this basically refreshes the fork.  

git pull upstream master  <— This will update Liz’s forked local master with Alison’s up-to-date github master copy.  

git remote -v   <— This will tell you who your local repo is wired up to (what the url is).  

HEAD is a token that we can reassign and it’s the “one we think of as being most in the lead”.  It’s basically the new stuff.  The BASE is basically the old stuff.  


Brian’s CSS Design Lecture

Having a basic photoshop understanding is a good thing, a lot of design documents come to you as .psd files.  Sketch is a special piece of software that is specifically for web design.  

Design specs that you’re going to get from clients vary widely in quality, sometimes you’ll literally get a sketch on a napkin, sometimes you’ll get a great looking static design that you then have to slice apart and put back together as a webpage.

Right now we’re doing a bunch of playing around with elements and moving them around to see how they look..  having some sort of roadmap before you get started is a good idea.

I’ll have to link the video for this lecture when he’s done because it’s pretty good.  

The basic gist of a website is that there’s always:

A header

A footer

Some content in the middle

There’s a million variations on this, but they all have the same basic elements, and the html for them looks pretty similar at the structure levels.

margin: 0 auto;  <—  full width header and footer containers

www.crossman.com has these, there’s an invisible container that holds all the content in the middle and has xxx pixel size, but the headers extend the width of the page

A standard website right now is ~960 pixels wide.  It’s really simple to work with because it’s nicely divisible lots of different ways, works well with 2, 3 and 4 columns and looks good.

http://i.imgur.com/pCOyGE6.jpg

Bootstrap is a framework that gives you a lot of this underlying grid stuff to start with which gives you a good starting place.

IF you understand the underlying principles behind bootstrap it can help, but it can also be a mountain of code that your’e now swimming in because you don’t know what most of it does.

Gutters - white space between components.  Should be a round whole number and the same across the page.  For our 960px page a 30px gutter works well.

whenever we see: margin: 0 auto;  <—  you should automatically thing that some large, structural component is being centered on the page.  What this does is gives the top and bottom a 0px margin and automatic margins on the left and right sides of the element.  Not for text, not for images (though both of those might be contained inside our structural element).  This is used for most/all of the content on the page 

Brian is building a modern header in codepen, I’ll link it here after he’s done.  

He’s going to do some ‘weird’ things here on purpose so we can see different ways to do things.  Basically the site will only ever have one < header> so we can reference the stuff that’s inside without sticking a bunch of unnecessary classes on everything.  

inside 
< body>

we then have

< header>

< header/>

< main>

Inside our main tag we put the big chunk of our site.  First our big middle banner item, then 3 conainers.  We use lists for these containers, no divs needed.  Putting them in another div would just needlessly complicate things.  

	< img class=“banner” src=“whatever”>

< ul>
	< li>some stuff in here< li/>
add 2 more list items for your boxes.  You can also put uls in here with lis as items that go in there, and then scroll through them by hiding one and unhiding the next one.  

< ul/>

< main/>


Work from top left to bottom right.  Just like with coding, you want to have a pretty good idea what you want to do before you start.  Another important bit here is to NOT add unnecessary containers, and it’s tough to know when they’re really needed or not for beginners.  But it just makes things needlessly complex when you can get by without them.  Basically if there’s a question of “do I need another container here?”  The answer is probably no, think carefully and try to use some element you already have.  

Normalize or Reset style sheets ~
A reset style sheet is just basic css that zeros out a lot of basic properties that overrides the browsers default settings and gets you a blank slate to start working on your site with.  

Right now we’re just building the skeleton of the beast, it looks like nothing on the page so far.  We’re going to put some placeholder images into it so that we can see what the site will /structurally/ look like later.

www.fillmurray.com <— is one example that is funny.

But don’t use those, the reason you shouldn’t is that the client really has no idea how you’re building out this code.  You’re building out a structure, it’s their job (the client) to provide the content.  

placehold.it/200x70 <—  this gives you a randomly generated image that is exactly the size that you want 

placehold.it/200x70/#ffffff <— any hex value here you want, use the clients colors for a bonus.  

You can put these images right into your site without actually making each one first, placehold.it will generate them as needed so you can make an entire mockup out of these images.  It’s really swag~

SO now we move on to css..

We have our boxes to start our layout (should probably fill in most of our page content before we actually start in on css but it’s just a demo)
First we put a background on things just to get stated, Brian likes gray a lot.  
Then he centers everything that’s supposed to go in the center via setting the width of the header div to 960px and applying margin: 0 auto; to it, and it immediately boops into the middle.  The background color automagically stays where it is, spreading across the page.  

Making nav elements display: inline-block; gives you a nice hybrid of the two properties, they take up the space of an inline element but can be moved around like blocks.  By giving them margins we can 


Font style can be chained together using just the font: css tag, look that up sometime.  

You can add your 30px gutter to the main element instead of sub styling all the things in there, it saves you some work later.  margin: 30px auto; and width: 960px;  

Getting our 3 boxes to sit next to each other, here’s how:

.sub_banners li:last-child {
	margin-right: 0px;
}

Footer Tyme

footer {
	clear: left;     <—  this makes it clear the above floating stuff 
	height: 150px;
	background-color: #888;
}

There’s some wonky behavior here as far as the float causing the bottom banner to be too close and not inherit the 30px margin from earlier in the css.  
You can just put a margin-bottom on the last element before the footer in order to get your margin back.  

.clearfix {
	clear: both;
}

This is a common convention, you then put a div anywhere in your html that you’re having weird float behavior and it’s really clear to you coming back to your code, and anyone else, that you had wonky float behavior and you needed to clear it.  

There are tons of ways to build this site, this is just one way to skin a cat.  But it’s a fast, clean version of a 960px site that is easy to make and we can duplicate it.  

Justified items are possible in css, look that up too.  Or copy Brian’s link from slack, along with the codepen in a minute.  

Lab today-

Is vague.  Woo~  Work on sales.html and index.html.  Use what Brian taught us to make a nice page.  You must use all of the images in the assets directory at least once.  

In Atom command+L selects the entire line that you’re currently on