#Code 201, Day 14 Learning Journal
###Thursday June 30th, 2016

Yesterday morning went smoothly enough, I enjoyed code review and Brians css demo.  I enjoy the demystifying process of "it's not magic, just work".  Anyway it was fun watching and learning more about key listeners in js and how they can be used to control objects in using css.  

Project Groups were set yesterday morning and we worked with them on our pages and merging exercise yesterday afternoon.  I'm a little disappointed mine didn't get chosen, but it was pretty ambitious and would have really required a team that /wanted/ to put in that extra effort to do something really cool.  So while I'd still like to be doing it, I'm also glad I didn't get stuck doing it with a team that didn't really want to work very hard on it so I ended up doing most of the work.  Anyway, after our lab yesterday we did some preliminary planning so it feels like we're mostly on the same page, we'll flesh out the skeleton of all the major pieces today and start working on them, and everyone will have some sort of deliverable for Monday.  

Joined Meetup last night, subbed to a few groups and generally looked around.  I'm not a very social guy outside of activities so having groups that are getting together to /do something/ is much better for me than 'hey lets go hang out' or whatever.  Anyway I'll keep an eye out for new groups to join and try to go to some sort of meetup here in Seattle once or twice a week.  

###Following the line break are my notes from the lecture.
---
Thursday June 30th 2016
Morning Notes

http://codepen.io/christopher4lis/pen/GqWBXv
This is a code pen Brian linked in slack as a demo of some of the capabilities of canvas and ?  basic 2d physics I guess?  Anyway it’s pretty cool.

Manhattan reactor B, tours fill up super fast.  What you do is call the bus contractor because even though the tour is full, there’s no real way to cancel online.  SO if someone has canceled the buy guys will know about it and they can get you a spot.  

We should all go to meetups I guess?  They’re important and helpful for getting integrated into the tech scene here in Seattle.  Set up an account and sign up for meetups in the tech scene.  CodeFellows hosts some of them ourselves.

Quiz 8 goes up tonight, due tomorrow night.  We’ll set project teams today after/when we pitch things.  Tomorrow we’re watching final project presentations for 301.  

Code Review -

When you’re tracking clicks it’s important to track clicks as they happen and so you’ll have their savory kernels to munch on through the cold winter.  

High Level JS overview woo~  

In 12 days we’ve moved from very basic variables and prompts to some pretty advanced topics.  So now what?  We’re going to take a look at what comes after in terms of the next thing to learn.

ES6 - isn’t the name anymore.  We now call it ES2015.  It’s the “latest and greatest” version of JavaScript itself, up to version 5 which was known as ES6.  But version numbers were too easy and too simple for those pretentious jackasses, so ES2015 was chosen as the name instead.  

ECMAScript - has something to do with ES2016 too.  

ECMA 5 / ES5 compatible is the JS we’ve been learning so far in this class.  There isn’t universal browser support for ES6 yet, and probably won’t be for a while.  caniuse.com is a good resource so you can see who supports what features.  

Node.js environment — allows you do use JavaScript on the server-side of the web stack.  JS was initially created to work as a browser based language to do browser things.  Node.js allows us to use JS in a not-browser environment.  It’s pretty great according to Brian.

Because Node.js can run outside of the browser you can be a full stack developer with just the JavaScript language.  It’s very powerful that you can do pretty much everything with just js so (most especially) when you’re learning you can develop apps fully with one language.  

IOT - Internet of Things.  A big pile of poorly supported and even more poorly documented apps and devices that have terrible security.  BUT they’re really cool.

Node.js is a neat bridge between mobile/remote access and IOT apps.  In particular it’s good at asynchronous activities, allowing the saving and retrieving of that persistent state really easily.  

Really understanding asynchronous programming and the different way of thinking about code, which we’ll cover a lot in 301, and we’ll even touch on it in 401 Python.  

Application Program Interface - API.  It’s basically the set of rules by which a program talks to the stack and vice versa.  

learnyounode - series of Node.js tutorials that starts easy and scales up to ‘really really hard’ really quickly.  

free ebook on the interwebz - eloquent javascript.  Covers a lot of what we’ve covered here.  Brian’s fav js book.  But maybe get a hardcopy?

JavaScript The Good Parts - another book that’s thin but dense and it’s referred to as “the bible” of javascript.  

Eric Elliott - another author who has a blog we should read / follow him on twitter maybe.  I should start a professional twitter acct for IRL use.  

jQuery - utility library for js that expands methods to do a lot of stuff.  All this DOM access we’ve been doing gets a lot shorter (for instance).  It does make things easier, but doesn’t give you a good back end understanding without learning vanilla js (which is what we’ve done).  

Brian’s CSS Demo - 

http://codepen.io/briannations/pen/xOdGAz

You can do basic animations just using JS and CSS so that you can make basic objects and animations without adding an additional library.  

The ball is going to move across the screen in a fluid motion - which is css.  The firing of the event to make it move is going to happen in js.  

Do not try to architect/program collision detection or physics in your final project.  You don’t have time to learn and implement that much in a few days.  

The background property can accept a passed-in url in css like:

background-image: url(http:yoururlhere.png);

you can also specify size, color, etc.  

Both the background: and font: support complex declarations but they require a specific format or you’ll F things up. 

Setting the Top and Left property gives you just 1 property to manipulate and keeps things simple.

The ‘change back to red’ part of the ball demo is a bit of a hack, it’s just reapplying the red color every 1500ms and isn’t actually checking for recent movement.  It was a quick, simple way to get the red color to reapply.

document.addEventListener(‘keydown’, animate);

don’t () the animate function, it’s called by the event you reference.  Using the ‘keydown’ event here you can use e.which in order to differetiate which key is pressed by #.  Use console.log(e.which); to easily tell which keys are which by #.  

The transition property is how we’re handling the animation but it doesn’t have any partial inputs.  

Challenge: refactor Brian’s JS code down to 20-ish lines.  

In order to make animations feel natural using css you’ll have to do some tweaking and testing.  It’s not a simple ‘set this up and run it’ thing.  

Basic rule of thumb for new developers: take however long you think a task will take and quadruple it.  Estimating is a very important skill in this industry.  

In JS there are differences between keydown, keypress and keyup that are important.  Any key press on keydown will give you an integer which you can then reference anywhere inside your JS code.  

if(event.which === 65) {alert(‘you pressed the letter a’);}

When you start thinking about a new project like this determining the things you need is important and building them out takes time.  We 

In CSS you can’t use top, bottom, etc properties w/o first giving the element a position of absolute.  In order to get the position to change you have to apply an initial position (can be equal to one of your settings), and then the transition and movement will happen.  

Moving the box to a click location is the same principle as this.  It involves getting the x and y position of the cursor and moving the box to that x and y position.  If you’ve applied a transition effect it’ll apply too.  
For instructions just google ‘cursor x and y position in javascript’  or ask for jquery.  

The goal in learning to code isn’t to copy other people’s shit, it’s to learn how to code and improve your skillset.  That said, you can’t code everything.  You have to draw the line somewhere and using other people’s code is inevitable.  Make sure to attribute where you got your code from.  Don’t just blindly copy and paste code.  

Lab Overview~

We’re going to make a git repo, make some pages, then get into a gituation (or a lot of them).

Always keep your master branch on your laptop synched up to the master on github.  You can also do a git pull origin master IN your feature branch and solve issues on your local side.  

the day 14 repo has lots of text in it, should look at that.  

https://github.com/codefellows/seattle-201d8/blob/master/class-14-js_inheritance-css_animations/git-team-workflow.md

The best way to avoid these types of things is that two people don’t work on the same file at the same time.  It’s the most common cause of these merge conflicts.  

The git terminal is pretty verbose, stop and read exactly what it says. 

Keep track of what your partner(s) are doing and communicate.  There’s nothing less productive than putting yourself in the situation where you’re constantly getting merge conflicts all the time.  

Take notes during lab.  You won’t finish the project, and the point isn’t for you to finish it.  The point is to get a group process going, set up comms, etc.  

Testing is one of those black holes in development where you can lose a silly amount of time and fixing the bugs that come back can be tough.  


Thursday June 30th
First Project Notes

3 interlinked pages
2 that accept user input

Simple matching game where we line match some words

Word familiarization pages where there’s a large picture with several words as boxes overlaid on the larger picture.  You click on the box that’s overlaid on the table (for instance) and the word will be spoken in english + XX language, plus the spellings for both pop up below.

Intro/Home Page

Simple landing page.  Cheerful introduction, introduce the Pictures and Game pages, maybe get the users name?  

Intro page will dictate the layout and global css variables for the other pages.  


Pictures Page

At least 10 items, we’re not sure which items yet but we can decide later.  The items aren’t important to the js coding side of things and can be filled in later.  

Frame = larger picture.  In each Frame we can do one item/word or several items/words, the programming isn’t that different, it’ll depend mostly on the art/pictures we can find or are willing to pay for.  BUT this needs to be decided before Friday afternoon so we can make progress over the weekend.  

We need to keep track of which pictures user X was shown and only show them matching game questions that involve the pics they’ve seen.  

Game Page

Simple item matching, several possible ways to match:

english words to XX language words

english + XX to picture

english + audio of XX  to  picture w/ XX label

etc, there’s lots of possible ways to do the matching part.  We just need to decide on one.  

Once matched they’ll briefly turn green then disappear from the game, to reappear below or beside the game in a “matched items” grid.  We’ll keep track of matches and wrong answers to score the user.  


Stretch Goals:
— High Scores/Separate results page
— Google Map (of areas where the language was used?)
— Language Sounds!!  
— List of words learned
— User Account?  