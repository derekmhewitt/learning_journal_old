#Code 201, Day 4 Learning Journal
###Thursday June 16, 2016

I'm going to treat this a little bit like it's a regular journal along with the learning part, just because I could kind of use somewhere to vent.  I'm commuting from Federal Way up to Seattle and public transportation is just a huge pain in the ass.  I tried the Sounder train but parking was a huge issue, I tried the Federal Way Transit Depot, and today one of the 'Park and Ride' things that isn't too far away from my house.  Anyway I've found another one that is close enough to the TD that a lot of busses hit both, and that bus drops pretty close to our building in Seattle (about a 15min walk away).  SO hopefully tomorrow I won't have to run for class just to make it on time :p.

As far as class and lab today went, I thought it was pretty smooth compared to the headache I gave myself yesterday.  During code review we got into a discussion about conventions for javascript and after thinking about it and trying it the way the convention dictates I think I'm going to try to follow that format from now on.  It makes sense and produces more readable code than mine did, I had too much white space and it was difficult to follow the logic.

Anyway for pair programming I was in a group of three with Erica and David.  We all worked pretty well together so that wasn't a problem and we actually got through all of our initial lab function adding in about 2 hours.  We then collaboratively rewrote my question #7 on the whiteboard (window, I had the pen and they helped) and Erica coded it in with input from both of us, since she was "Driving" my code.  Anyway it cleaned up nicely.  I spent the rest of the day cleaning up the comments and code to look closer to the convention I mentioned above and then played around with CSS a little bit.  We both also helped Erica a little bit, she was going for the 'stretch goal' of putting her answers into arrays and then having one function ask and respond to the first 5 questions.

If I have some spare time this weekend I want to go over some of the CSS tutorials and other articles that have been linked this week, but I just haven't had time out of class hours.  My commute is taking roughly 4hrs a day, I'm getting some reading done on the bus but it's hard to make up for that much wasted time.  I'm getting a new iPad tomorrow and that should help a lot, I'll be able much more easily read our books in pdf format and fill out the Canvas assignments right on the bus, along with some of the other linked reading that is recommended.  

###Following the line break are my notes from the lecture.
---
 Thursday June 16th
Morning Notes

Quiz one due tonight at 11:59 (I’m done with it), Quiz 2 will be published tonight and due Friday night at 11:59.

Today code review, css box model, break, JS functions and look at the lab assignment w/ pair programming.  

It’s important to error check your code, testing for various kinds of inputs.  Testing incorrect or unacceptable inputs is important.  

3 most important things to test for: zero input, single input and infinite input.  Empty = zero input.  Infinite input = all possible inputs.  

Lots of code review.  We don’t use break statements much because returns act as break statements and we’re usually returning something later on.


CSS
It’s important to keep in mind that there’s a difference between making things work and making things work optimally.  

All of your HTML code is a box.  Inline elements can be treated as block boxes by css and block boxes can be made to display like inline elements via css as well.  Even inline elements are boxes, they just flow in line and their box is the size of the content that is inside them.  Boxes can have width and height, color, borders, etc but no matter what shape they take on the screen via CSS wizardry they are still boxes and will behave as boxes.  

Generally speaking we don’t want to fix the height of any boxes.  The content dictates the height of the box, if you change the font, display size, etc and fix the width, the box will do wonky things with a specified height.  A min or max height is ok, but fixing the height is probably not a good idea.

Use fixed widths instead, either in pixels or % of the screen.  

Border + Margin + Padding
Every box has a border around the content inside, even if it’s invisible.  The Margin is the extra buffer outside the Border, the Padding is extra space on the inside of the box that pushes the Border outwards, making it bigger.  All together these 3 things dictate how boxes will interact with each other on a page.  

Content + Padding + Border + Margin = the complete size of the box.  

Borders extend the size of the box.  Use an Outline property instead to visually see the structure of your site while you’re building it, but never use them in production code.  

Brian’s go-to outline property is a 1px dotted line border around every element on the page (because no one is ever going to use that on an actual page mkayy).  

 * {
outline: 1px dashed orange;
}

We do a lot of our css work in the dev console inside Chrome itself instead of swapping between Atom and moving back/forth.  

Thursday Morning #2

More CSS and Boxes

If you center an element it centers within the element that it’s inside.  

You will see this convention all the time:

margin: 0px auto;

I can’t explain the details of this, Brian covered it really fast.  You can use text-align: center to center an image, as long as you use it on the container the image is in (first parent) instead of the image itself.  

Top Right Bottom Left is the notation rule for CSS so saying 0px auto is specifies Top and Right which are automatically duplicated onto Bottom and Left by the software.

Change Inline/Block
By changing the display property of tags you can change them from block to inline and inline to block.  There is a default browser margin that is (sometimes?  always?) applied to inline blocks (which we will learn to get around later by overriding the default).

Lists don’t have to be a list of text, un/ordered lists are a really hand thing.  They can be a list of links, a list of products, a list of.. whatevers.  It’s also handy because you have a built in container in the < ul> or < ol> tag.

We’re dealing with a huge amount of new information and trying to mentally digest is all is difficult.  It’s easier to group and classify those things, and remember them as associated terms.  We’re going to do some of that here.

Every HTML element has a “static” default position property.  

Other position properties:
Normal, Relative, Absolute, Fixed, and Floating
Each of these has their own special behavior.  The Static property mentioned above === normal.

Relative positioning is going to start with it’s Normal positioning and nudge it a little bit from there.  It can be thought of as a subset of Normal because it’s tied to the elements Normal position.

Absolute positioning takes an element out of normal flow and anchors it to an absolute spot on the page.  Absolute images scroll onto and off of the screen, think of them as being anchored to a specific spot on the back of the canvas.  
Brian - there is basically one reason you use absolute positioning.  You use it to anchor things onto the page.  He pretty much never puts a position of Relative on anything.  When we set an element to Absolute positioning we are positioning it relative to it’s first parent and then we can move it around however we want.  Remember the t-shirt and t-shirt label example if you can.  Moving the banner/price label around on top of the shirt is done using absolute positioning.  

JS Functions()

Functions are a structure we use in javascript to put a wrapper/container around some kind of behavior or logic so that we can “call” it later without having to repeat the code.

var myFunction = function(pass in information here for example A, B) {
some code here to be executed with A and B
example
var C = A * B;
return C;
}

in order to call the function later use:

myFunction(X,Z);

where X and Z are values to be placed into A and B in order to return C.  I know Return acts as a break; and terminates the loop (if there was a loop in the function) but I’m not sure where the information actually goes or.  I’m assuming that when you call a function you will store it in an array or otherwise use the output C immediately, such as:

myFunction(X,Z) = D:

Tomorrows lab is all about getting stuff into and back out of (returning) things from functions, so just wait until tomorrow.  Today’s lab is about focusing on the logic of the function itself and pair programming.

Pair Programming
It involves a bunch of little things.  You have to communicate together, you have to make decisions as a team, whose computer are you going to use?  And then there’s the GitHub piece.  There is a good set of instructions in the class repo.  