#Code 201, Day 6 Learning Journal
###Monday June 20th, 2016

Lecture this morning was good, I took a bunch of notes and even more from Sam's afternoon 'how to put your tr/td into the DOM' lecture.  

Working on this code was actually fun, I enjoyed making the constructor function and putting the pieces together into the final product.  Working on the stretch goals was interesting and I learned a few new things: 

---
####passing variables between functions (even i used as a counter) is easier than I would have thought.
---
####Nesting multiple FOR loops to access nested arrays is possible and interesting, but hard to keep straight.  Write things down and work your pseudocode until you have a solution on paper, then use that logic to write your code.  
---
I'm experimenting with formatting a bit here so we'll see what sticks...

The footer function is the one I'm most proud of defenetly, it took longer than any of the others and the totals really came out nice.  It's also dynamic so if you change any of the inputs it'll adapt nicely to that change and just output more or less table cells.  I think that making pages that respond dynamically to inputs is interesting because it's less of a static output and more of a (some stuff goes here, design a way to take this stuff:()XYZABC) and put it into that not-static hole).

###Following the line break are my notes from the lecture.
---
Tuesday June 21st 
Morning Notes

Quiz 4 pub’d today, due tomorrow night.  We’ll go over 2 + 3 in a few minutes.  Going over the days agenda.  

Review of yesterday’s project - Sam is going to build it live so we can see it and ask questions.  1 shop location.
Good chance to really think about and consider architecture.  

From project building: if you see an empty array [ ] somewhere in your code you should automatically dial in on the fact that, at some point, you’re going to use that array to store data.  

We’re going to want to add location name into our constructor function.  Later on we’ll add “identifier: ‘firstandpike’ properties to our objects to use it to assign an id or class to some of our html objects.  This is already getting pretty complicated :p

We can inspect variable by entering it in the console.  If we enter console.log our code prints out the same output for us to access in the console.  console.dir(yourThingHere) shows us the object as the object, and we can open the arrays as trees and really see what is in there and (if things are broken) where they broke at.

What is the __proto__ thing at the bottom?  Just part of the browser?  idk

Building methods outside of the object (using dot notation) is cleaner looking than using the literal format but does it work with the constructor function?  

Pushing things from js -> dom is ‘rendering’ them, or that’s one way to say it anyway.  

(objectName.andProperty).push(varToBePushed); <— this will store a variable in an array, adding a new value each time it pushes

A shorter build -> check process would work better for me I think, that’s what Sam is suggesting.  Don’t build big pieces of code before checking them.  

console.dir(someThingHere) <- is your friend

Round down cookies, there’s no crumb sales here.  

Sam put the calls to his previous functions inside previous one, which I feel like has upsides and downsides.  Upside is that when you’re done writing everything you can call all of your methods via just 1 command, but the downside is that nesting them that way might obfuscate where your methods are called at later so that for anyone else coming back to look at this they’ll have extra work to do to figure out where you executed which parts.  I’m not sure which example is best?

The demo will be in the class repo for us to look at during lab.  The Math.random() function could be a global function/method of a helper object that we just call so that we don’t have to rewrite it inside every one of our project objects.  

Tuesday 21st Note #2

Constructor functions woo~

We’re also going to replace the lists in our project with a single table where we put our cookies per hour into table data spots.  This could be tough to get working?

The table layout is in the repo, Totals go in first column and going across is each hourly # boop boop boop

There’s a stretch goal to get the Totals column at the bottom of the table to get it all working.  

We have stretch goals for the public facing page, more images in our repo to help us and we can work on a style guide(?) which we can ask Brian about.  

There’s a demo in our repo for today too so we’ve got that to look at if we need it.

Constructor functions make objects via passed in arguments, so you don’t have to write as much code.  There’s demos in the book and on the internet too, if you need help.  

Sam - The key to understanding constructor functions is understanding that a constructor function looks a lot like objects in literal notation.  We just adjust the references so that they apply to this.aThingHere.

per example:

function Student(firstName, lastInitial, faveNumber) {
	this.course = ‘201d8’;
	this.firstName = firstName;
	this.lastInitial = lastInitial;
	this.faveNumber = faveNumber;
	this.isCodeNinja = true;
	this.introduction = function() {
		console.log(some introduction here);
	};
	console.log(this);
	myClass.push(this);
};

In order to make a student using that constructor function we use:

var myClass = [];
var alison = new Student(‘Alison’, ‘Z’, 16);
var david = new Student(‘David’, ’S’, 19);

the myClass array here stores the student objects inside, so we an access and otherwise use them as a group, we can work through those objects with a for or while loop, etc.  Storing them inside a container gives us lots of ways to do stuff to our array as a group.  

Constructor functions allow us to save huge amounts of code because we can construct the objects by passing in arguments.  You can still add methods via dot notation or otherwise modify your objects, they’re still regular objects and are not different than objects created via literal notation.

wtf this ?  

THIS in a global context refers to the window object.  It is context-dependent, which means when you use it inside a constructor function it means the object that the function creates.  When you use it in other functions it refers to its immediate parent function.  

console.table creates a very nice table console that represents the objects with an entry

You can use console.log() with a , instead of a +.  When you use a comma the output goes on the next line and it’s easy to see your debugging statements.  The CONSOLE is an object. The .log part is a method of the console object, and there are a bunch of other methods available to you.  DOT notation like this always tells you the thing to there right is a method of the object on the left.  The console is just one of many built in objects in javascript.  

Adding to a constructor function:

Student.favoriteTA = ‘Nadia’; <- if you enter this after the constructor function it will change the Student object constructor, but it would need to be put above the constructor function in the code in order to work on the student objects you’re making.  

Student.prototype.favoriteTA = ‘Nadia’; <- this one will work from anywhere?  it’s contained inside the __proto__ subject

Prototypal Inheritance - is a big part of javascript and front end web dev as a whole.  Everything inherits from it’s parents in a structured way.  Prototype properties will be inherited by their parents IE: with a prototype value added to that declaration, all Student objects will have a live prototype key of favoriteTa with value ‘Nadia’ immediately after that line is written into the code.  

We’ll go deep into prototype inheritance next week.  

So for our bigger functions from the cookies part of the assignment we can still write those functions outside the student method, then just add them back into the Student’s prototype object (or whatever our constructor is named, it won’t be Students).  


SO now lets talk about Tables.  Woo tables~

Sam has made a table of the cats in his neighborhood.  That’s not creepy right?  Anyway the demo is in the repo.  It seems like the browser adds a <tbody> tag of it’s own even if you left one out?  That’s strange.  Looking at it in the dev console way is a good way to ensure that you filled everything out correctly and it’s all inheriting downwards correctly too.  

Things to put element into DOM: 
 (if you’re putting it somewhere you also have to document.getElementById on the thing you’re putting it in)
1 - create element
2 - give content
3 - append to dom

Tables are made in JS via typewriter kind of functionality.  You’re going to go row by row across a table.

So for the TR you’re going to grab the place it’s going, make the element, and then stick 3x TD opening and closing tags in it, then it’s own closing comment.  You have extra stuff to do here.  Basically you’ll make a For loop that adds TD tags for the # of elements you need and then adds a closing tag.  There are some more pieces of this in the demo for todays lab so we can look through those and Sam is going to do a demo of it for us around 1:30 or 2pm so we’ll get a good look at the table demo.  


Here are the starting numbers that you'll need to build these objects:
Location	Min / Cust	Max / Cust	Avg Cookie / Sale
1st and Pike	23	65	6.3
SeaTac Airport	3	24	1.2
Seattle Center	11	38	3.7
Capitol Hill	20	38	2.3
Alki	2	16	4.6


Tuesday 21st Note #3
On JS Tables and dynamically creating them woo~

Toeny is spelled correctly, we’re going to make a table with him in it using javascript.  

We basically have to build the table top - > bottom row by row in JS in order to have the HTML come out right so that the table comes out correctly.

<table is=“cats”></table>  <- creating one of these with the ID where I want my complete table to go is an easy way to get a spot to put your js output.  You /can/ add this later but it’s a big pain in the ass.

for(var i = 0; i < allCats.length, i++) {
	console.log(allCats[i].name;
}


var catTable = document.getElementById(‘cats’);  <— ‘cats’ is the id of the place where we’re going 

Best Practice Syntax: trEl <- the El tells you it’s an element and it starts with the element name in lower case, so in this case < tr> for table row.  < td> would be tdEl

var trEl = document.createElement(‘tr’);

var thEl = document.createElement(‘th’);
thEl.textContent = ‘Name’;
trEl.appendChild(thEl);

var thEl = document.createElement(‘th’);
thEl.textContent = ‘Color’;
trEl.appendChild(thEl);

var thEl = document.createElement(‘th’);
thEl.textContent = ‘Tail’;
trEl.appendChild(thEl);

catTable.appendChild(trEl);

The above is one way to do this.  We could also do it with a For Loop such as:

var headerTitles = [‘Name’, ‘Color’, ‘Tail’];

for(var i = 0j, i < headerTitles.length, i++) {
	put those 3 lines in here but use headerTitles[i] instead of Name, Color, Tail
};

catTable.appendChild(trEl);  <—  After either method this is the way you put the table row into the html.  

We can make something like our above for loop to make the rows for our stores in our project. Woo~

We can also write a for loop to access our cookieStores array [] and run through so that you pull the information out of each one via the array and into td cells.  This means you can format 1 row and it’ll iterate for you along the table..

Different example:

var catDataArray = [];
for(var i = 0; i < allCats.length; i++) {
	var oneKitteh = [];
	oneKitteh.push(allCats[i].name)
	oneKitteh.push(allCats[i].color);
	oneKitteh.push(allCats[i].tail);
	catDataArray.push(oneKitteh);
}

text.Content = empty string <— google this, it’ll give you an empty cell for the top left of your table

our header row will be a standalone global function.  For each location you’re going to do the create -> give content -> append cycle 
we need it for the store name, the daily location total, and a for loop to run through the times

The totals row?  That might not happen today, it involves traversing the DOM and is more complicated.

We could also add a “render” function that makes the row for that individual cat and storing it in an array [] so that we can just get it from the cat by grabbing that array and iterating through it.  If you do this you’ll have to add the cookies @ time TO that array as well.  

Cat.prototype.render() {

}
