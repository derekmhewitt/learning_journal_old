#Code 201, Day 8 Learning Journal
###Wednesday June 22nd, 2016

Lots of notes from today.  I'm not really sure what to reflect on or journal about..

I learned a new shortcut today that I'll try to remember, after tabbing into a document a few times you can shift+tab to move backwards one tab space at a time.  This means you don't have to delete all those spaces. 

control + command + arrows up/down moves whole groups of code in atom.  I forget how to select the current line the cursor is on via the keyboard though.  If I get a free minute tomorrow I'll have to look at the atom shortcuts again tomorrow.

Lab today went pretty well, I wrote up mostly how it went after and put it in the submission for that assignment.  I feel like Valerie made some good progress, hopefully she learned something from coding with me and maybe picked up a few more tricks.  

The lectures and examples were very helpful today, I referred back to everyone's example at least once.  I didn't get to do an event capture that stemmed off the DOM object for the event (like Sam did in his demo), I'll have to try it that way next time.  Just getting everything working on both our pages in lab took up the full time allotted.  

Anyway I'm tired, going to get to bed at a reasonable time tonight.


###Following the line break are my notes from the lecture.
---

Wednesday June 22nd
Just one big note for today I guess, I forgot to make several.  Whatevs~

Got the email from CF admissions, and another one from Mindy so I should be set for 301.  

Schedule:
- Code Review
- Events w/ Nick
15min break
- HTML Forms
- Lab Overview

Code Review~

We can make a “.gitignore” (file or directory?) that we can put file names into which git will then no longer track.  This does not untracked files that were already tracked, if you want to remove files entirely that were previously tracked ignore them first and then remove them from git so they won’t be re-added.  

Loren Ipsum is great and there’s lots of places to get it on the internets.  Bacon Ipsum and Samuel L Ipsum are good examples.

Brian - typography is becoming more important in the web industry, and you want to use fonts that scale well from very small to very big fonts.  We’re using more svg fonts than ever before.  Use readable fonts that add to your page and work well with your design.  Your design can’t stand alone, you have to design something that not only makes you happy, but makes the client happy and that the end user likes, finds easy to use/read/interact with.  

Sam - generally speaking, executing code in the global space isn’t a good practice.  Wrapping the things your js is doing in functions and then calling them in the order you want is easier in the long run, and a requirement for asynchronous programming which we’re going to start doing today.

Top to Bottom Structure:

Data
Functions
Function Calls

This is a pattern we’ll see in smaller blocks of code too, when doing your construction function you put in data first, then add functions, then build your objects using the constructor function here.  

We will probably want to assign an ID to each one of these rows?  Possibly by adding a property into your constructor function.  You might also want to add in address, phone #, etc.

You don’t need to redeclare variables multiple times, and declarations are limited in scope.  You do have to pay quite a bit of attention to where you’re working at and ensure that your local vars are used properly and you don’t overscope them.


Events w/ Nick~

Events are things that happen, in the context of your browser they’re things that the page does (like finish loading) or the user does (like click things).

We make use of these events by using event listeners and event handlers.  When we grab an event using one of these methods we then do something else based on that input.  

Nick is going to put his notes on github after we’re done, so you’ll really want a copy of those.  Maybe just copy the whole repo lol.

You can use event listeners to do just one thing or multiple things.  Set the target of the listener, do the thing, and then append it to the page.  

Some events have a default behavior, and it can be very useful to prevent that using preventDefault(); <— it’s a method of the event itself.  

Convention is to call the event “e” var name, but “event” is less ambiguous and easier to learn, so I’ll probably use that for now.

The process we’re using to do this is a lot like what we did yesterday for making rows and td cells.

Form Validation~
Once we have a form we need to validate the input if we’re going to do something special with it, we have a bunch of big logic that helps us do that.  

Something to reiterate on again - plan out your code before you start writing.  You should have a pretty good idea what you’re going to be coding before you start in on a block of code.  


Brian’s section on Forms~

When we talk about forms there’s 1 thing we need to poke first, and that’s the Form element itself.  It’s going to wrap all of our subsequent items.  The action attributes like post or get allow you to do things with just the html without using js yet.  

REST architecture - Representational State Transfer, we’ll cover this in 301 woo~

<form action=“path/to/go/to” method=“post”>  A form goes here </form>  <— for right now we’re going to exclude those attributes, those are for sending data to somewhere else.  We’re going to focus on working with he data we receive right on the page we’re currently on.

<form id=“myForm”>
	<fieldset>
		
		Some series/set of form elements here

		<label for=“first_name”>First Name:</label>  <— Our FIRST_NAME here is tied to the NAME= attribute of the below input field, NOT the id
		<input id=“first_name” type=“text” name=“first_name> </input>   <— textboxes are the most common types of input fields

	</fieldset>

	<fieldset>
		if you have a 2nd (or more) inputs to collect and they look wonky use a 2nd <fieldset> to put them in their own containers

		<label for=“last_name”>Last Name:</label>
		<input id=“last_name” type=“text” name=“last_name” placeholder=“Last Name”> </input> <— the placeholder will NOT fill the form, it’ll put a grayed out version into that empty element.  The VALUE attribute will allow you to put an initial value in that box which then must be removed or modified by the user.  The value is not required to be present as an empty string, but all fields essentially have value=“” as their default, which is an empty string.
	</fieldset>

	<fieldset>
		<label for=“stuff”>Do you like stuff?:</label>
		<input id=“stuff” type=“checkbox” name=“stuff” value=“yes”> </input> <— the value=“yes” here gives it a value of checked.  It’s no by default?  
	</fieldset>
</form>

You can create buttons several ways.  The <button> tag makes a generic button with no default action, the <input type=“button” value=“label_here”> <— makes a button that submits the form it’s currently in, but only if it’s inside <form> tags.  

Don’t nest a form inside of another form, you will break things.  Use two separate forms, you can always submit information from one to the other.

var myForm = document.getElementById(‘my_form’);

//do nothing yet, listen for submit event
myForm.addEventListener(‘submit’, function() {
	//once submit event happens, do this stuff
});

An anonymous function is just a function without a name.  A better pattern/convention is to name your function, for a couple of reasons - you can reuse event reactions, and once you have a bunch of anonymous functions it gets hard to read and figure out what’s going on.  

Event delegation and bubbling is something we’re going to handle later and defaults to false, we’re going to leave the default in place and just not declare it.  False is always implied on the end of your listener/event handler like this:

myForm.addEventListener(‘submit’, function() { }, false);

So we don’t need to explicitly declare it each time.

Brian is building his form in a straightforward manner line by line and mentioned that it’s important to go about things in a procedural way.  Develop a method that you use to go about writing code methodically.  

You can declare multiple variables w/o reusing var by separating them with a comma and a semicolon after the last one.  

Step 1 - 
Access the Form
Step 2 - 
Setup an event listener that grabs the submit
Step 3 - 
Grab the value of each form element and log it to the console.  You can send it anywhere you can see it, but debug the form before you move on and get a really complex bug 

console.log(‘here’s a method to log’, some.objects.data);  <— using a comma is easiser/faster than the + and concatenating, especially for debugging where the appearance doesn’t matter as long as you can understand it

on the initial <form> tag adding an action=“some/path/here” will redirect you to that submission path and changes the functionality of the form

it’s common on forms to use event.preventDefault(); on the first line of your submission gathering in order to make sure that you grab all of the data you want, then have some sort of check or prompt to confirm that you have all of the data you need before submitting.


Styling your pages and subitems is something we don’t care /that/ much about yet, but here’s  cool way to make your tables look better:

look at some of the css from Brian’s linked codepen and 

in css you can exclude the px or other measurement if the # you’re putting in is 0 (ZERO)

Example attribute selector:

input[type=“text”] {
	This selector will grab any element in the html with the attribute “text”
}

When you want to make custom select boxes, check boxes, etc don’t try to modify the ones that already exist.  You have to do something hacky and we’ll cover that later probably.  For now just stick with what we’ve got.  

input[type=“submit”] {
	This will grab things w/ the attribute tag of “submit”.
	border: none;
	padding: 8px 12px;
	border-radius: 3px;  <—  Don’t get crazy with this radius, it’ll look wonky
	color: #fff;
	background: #444;
	transition: 750ms all;  <—  this works with the :hover and background: #888 on the tag below
	cursor: pointer;    <—  this gives you a clicky pointer over the submit box so try to use this on buttons
}

Use padding to balloon your element out and make it take up the larger space that you want it to fill in your design.  

input{type=“submit”]:hover {
	This will add a hover effect to our button
	background: #888;

	CSS3 has given us a lot of background animation defaults.  JS animations run relatively poorly in the background and look worse, running slower.  It’s also easier and faster to make these in css than it is in js.

	the TRANSITION attribute added to the “submit” tag above will give the button a nice fade in/fade out effect 
}

Right now don’t even try to style pulldowns, radio buttons and text boxes.  We’ll get to it later, but mostly just leave them alone because ensuring cross-browser compatibility is almost impossible.  We’ll get to other methods to do this later.

http://codepen.io/briannations/pen/RRoyaq?editors=0011   <— codepen demo to go along with these notes

Sam - went over a premade demo of forms

the someObject.forEach  <— look that up and see what it does.  Alternative to the for loop?

when using a form or other asynch action the user makes, when you call a named function you can’t pass in arguments, and having (); at the end will do wonky things (like call the function on page load).  If you want to pass in arguments you have to next an anonymous function inside and pass the arguments to that.  

when we go to handle our event we should console.log(‘the event said’, event); early into our function to give us some idea what’s going on.  Events are complicated objects created by the page that have a ton of properties by default, and even more prototype properties too.  Look at Sam’s example to see the other event logging options, there’s several more.

event itself
event.target
event.target.says
event.target.says.value <— this is the actual textbox output sam was collecting.  We can put an id on the field and it get that way, or we can pick the event fields directly from the dom rather than cluttering up the html with a lot of ids.  

Building in field clearing into your event handler function is a great awesome thing.  Sam also pushes the constructed event objects into an array as they’re constructed, then displays them in another array?  I forget how he did it exactly.  He clears the display and re-displays it again after each new comment so that the old comments aren’t repeated each time and you only have 1 list with the newest comment at the bottom.  
