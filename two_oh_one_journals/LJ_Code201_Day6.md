#Code 201, Day 6 Learning Journal
###Monday June 20th, 2016

Class this morning was pretty good, we didn't run over time.  Commute was overall pretty good too, I think I've mostly got the right bus route figured out.  We covered a lot of good information in class and I took pretty good notes.

Writing the lab this afternoon I can see that it's pretty easy to get too lost in the forest and not see the trees anymore.  I made a lot of silly syntax mistakes when I initially wrote a bunch of my code, hopefully just practice and repitition will help with getting that nailed down.  I've still got a ways to go on the cookie lab and I will probably have to work on it at home for a while tonight.  But I think everyone will, this is a big lab and a LOT to try to get done in just a few hours.  Even if you knew exactly what you were going to build and how to build it typing all of that into atom in just a few hours would be a tall order.  

I went over and listened to Brian's css demo this afternoon of the exercise he gave us on Friday, it was informative.  I spent about 90min on it yesterday and didn't even get everything to sit right where I wanted it.  I just overcomplicated the whole exercise by trying to absolutely position all of the elements and floated some of them left and others right, it made moving individual ones around very difficult.  It seems like if you don't ever fall into that trap positioning is a lot easier - apply a reset style sheet, build a box to hold your content (either in pixels or out of %) and just start throwing it in there.  After it's seated in place you can start modifying shapes so it's important to be able to not only see the boxes but understand what the boxes can turn into later (which is just about anything via css).  


###Following the line break are my notes from the lecture.
---

Monday June 20th
Morning Notes

Wooo we survived week one.  Yay.  Now we get to watch a funny vine.  

First of all going over class surveys.  We had a slight snafu here, comments are coming onward hoo.  

Get help, 15min rule during lab.  Don’t struggle, ask for help and don’t bash your face into a problem alone.  

Wednesday we’re covering forms, so starting then we’ll be able to get user input from those.  Goodbye prompts and alerts.  

Nick - Domain Modeling readings

Starting with the smaller article I’d read a few days ago (early last week).  When you understand what it is you’re trying to do you can write your code a lot easier.  It’s much easier to think through the problem first and then write code, than have to stop and rethink the problem in the middle.  The problem in the article is a small, set problem that the author uses in several languages to teach students about their differences and similarities.

The longer bit from github was a good blend of problem domain and the current spot we’re at in class using the constructor function for objects.  

Are there any problem domain worksheets or trees that are commonly used to fill out the inputs and outputs you’re looking for?  
Sample RPG character:

var character {
	“experience”: 100,
	“level”: 100,
	“items”: [‘lamp’, ‘rope’, ’sword’]
	“health”: 50;
}

You could have any other attributes you need or want in order to make your character functional.  You could even have a constructor to make multiple character objects, it depends on how many you need.  Once you have your character objects you can have them “move around”, “gain experience”, etc etc using methods?  Or any other 

You can have quotes around js key names via JSON which we’ll go over next week I guess.  When you have quotes around the keys you can use “non-legitimate” js keys in your key:value, pairs because json is going to handle them.  

Sometimes object notation will involve brackets so you can’t just assume that because you see [ ] that you’re working with an array.  Just keep that in the back of your mind that you’ll have to look at the context and determine what sort of data you’re working with.  

Most of the time, at a large company, you’ll have a more planned architecture from which to hang your individual bits onto.  Problem Domain Modeling comes in big during that conceptual phase, we’re focusing on a very small version of it here in order to just keep things simple.

Ultimately in js everything is an Object.  Arrays are objects with numbered keys where [0] is the key to the value in the first spot and the things in there have a specific order.

DOM - Document Object Model

The DOM is basically your html document, or is most closely related to the html anyway.  The DOM is a tree structure where your html sits and it represents your html and is tied to it.  You can take static snapshots of the DOM or have a dynamic version that stays up to date with changes.   Using chrome you can expand the tree and see the branches.  

The document node is the highest node on the DOM tree except for the window itself.  Ultimately what you have here is a tree representation of the page so we can work with the elements within using js (and maybe other languages later?).  

There’s 3 things we’re going to use the DOM for:
Selection, Traversal, Manipulation

Selection - we can select a particular object in the DOM using certain js methods

Traversal - We can traverse the DOM and move from our current selection to other selections

Manipulation - We can change data that we’ve selected using the DOM

DOM manipulation is one of the key components in front end development.  We have lots of interactions that use dom methods to interact with the page and the user.  

Right now we’re going to be dealing with vanilla js and a vanilla dom, later we’ll move away from vanilla and use jquery instead to do most of this stuff.  We need to understand the basic js first and we’ll move into jquery in 301.

The DOM is called an object model because the model is made of objects - you can select and work with all of them as objects because they are.  Elements(objects) are nested mostly like they are in your html.  

An attribute is anything that provides your html with additional information; a key:value pair.  

The easiest way to select items in the DOM is to just use an id so that you can select it exactly.

document.getElementById(‘firstElement’)

.getElementById = a method(function) of the document object.  The document object is built into js and the browser for you to use, along with a # of other basic objects.

The window is the highest level object in the dom and we typically exclude it and just reference document.getSomething

Live code demo:

var body = document.getElementsByTagName(‘body’)[0];  <— has to be assigned to array location because that method .getElementsByTagName will return an array

body.innerText = text inside the body element
body.innerHTML = html inside the body tags on the page

If we do this it’s going to remove whatever was there and replace it with whatever we add using these methods.  

document.getElementById = easiest way to interact with the page.  Only 1 id per page of a given name so you will always select exactly what you want to change or update.  

var update = document.getElementById(‘update’);

update.style.display = ‘none’;

There’s a literal ton of stuff that we can do using these kinds of manipulation, but we’re just going to focus on getting one element that we want by id and changing it using a few basic methods for now.

Next Brian programmed a button to modify some text 

Events are the driving force behind DOM manipulation - events being user interactions.

w3schools has some great demos on these inside the JS Tutorials section so you can look through those later or if you get stuck.  

When you use getXXXX method if the name is plural IE: “Elements” vs “Element” the output will be an array and you’ll have to specify an index to use/store/interact with that output IE:

document.getElementsByClassName(‘blurb’)[0];  <—  will select the first html element with the class of blurb.  

Using the DOM we are not actually modifying the html file, we are modifying the live version of that HTML that is stored in the browsers memory.  



Monday Note #2
Tomorrow is object constructors, today is object literals.

Object literals are as simple as declaring a variable, giving it a name and  { } for properties (key:value pairs)

var someObject = {
	color: blue;
}

Objects allows us to bring together all the properties and methods(functions) of a real world noun of some type into one code Object so that we can use them together and use them easily.  

Think about methods as being like behaviors, things you can do with your noun of choice.  Using our hotel example from the book, you can check availability and book rooms in a hotel.  

3 things that are hard in coding:
Naming Stuff
Cache Invalidation
off-by-one errors

so we’re doing a codepen live demo here:  http://codepen.io/samhamm/pen/wWzQxb

I’m not sure this link will persist all that long but hey, we’ll try including it here.  Anyway we’re stuffing a bunch of data  into an object using literal notation.  You can do this via:

class201 = { };
and then 

class201.students = [“some”, “student”, “names”, “here”];

or this way:

var hotel = {
	key: value,
	key: value,
	key: value;
}

When you have simple key:value pairs to add to an object the second method is really easy to visually see, assigning longer methods via dot notation is probably preferable (for now at least) in order to keep visual continuity of your code more easily.  In { } bracket notation longer methods get really confusing having them inside your outer curly brackets.  

  You can treat items in arrays like they’re strings and pull individual characters out using a 2nd set of [ ] to do it.  


Following along

HTML File

< h1> Code 201 - June 2016</h1>
< h2>Students</h2>
< ul id=“studentList”></ul>

< h2>Instruction Staff</h2>
<ul id=“staffList”></ul>


JS File - taking js information and rendering it into the DOM
4 stage process:
1: access the dom element where we’re going to put our information inside of
2: create the html element
3: give the element content (which in this case comes from our array)
4: attach or insert the element into the dom


working off our larger code demo linked above

//access the dom element where this will go

var studentList = document.getElementById(’studentList’);

//create the html element

var listItem = document.createElement(‘li’);

//give the element content

listItem.textContent = june201.students[i];

//attach/insert the element into the dom

studentList.appendChild(listItem);


For our lab we’re going to make sales.html and index.html.  The sales one is our focus for today, just throw something into the index because we’re going to build on the sales page w/ the index tomorrow.

Separate object in literal notation for each store location.  We’re going to simulate cookie sales via Math.random(); with timed outputs.  Using average min and max customers per hour we’ll get a random # of cookies sold and then do the next thing with that.  

Google Fonts - just literally google “google fonts” and you can use any of those for free with attribution, just copy and paste the extra information there into your readme and that’s the attribution you need.

Math.random(); returns a number between 0 and 1.  Google this: math.random man and it’ll show you how to get a random # between X and Y including X and Y, so just go look it up.  

You shops might look like:

‘’’
var capHill {
	min: 12,
	max: 18,
	avg: 14,
	hourlyCookies: [ ],
	hourlyCustomers: [ ]
}
‘’’

and we’re going to need JSarrays.push or something like that.  