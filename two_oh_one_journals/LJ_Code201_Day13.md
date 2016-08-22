#Code 201, Day 13 Learning Journal
###Wednesday June 29th, 2016

Lecture was pretty good today.  Sam went over lots of the pitfalls from yesterday, Brian gave a cool css demo, we went over lab and pitched projects for project week.  I pitched an asteroids-like hybrid game, maybe it'll get chosen?  It might be overly big for the scope for a 201 project though.  I'll do some research tonight on phaser.io and see if it might work for that, and if it has enough supporting documentation and such to be possible to make that game in a week.  

Working with localStorage is difficult but we got it working.  Everything in there is a string, gotta remember that ><.  I also broke my chart somehow, the crazy bit is that it was working yesterday?  I really have no idea how that object /was/ working before and broke today..  Anyway now that it's inside the chart drawing function it's working.  I got 3 chart bars showing and figured out how to change their color, I also found the startAtZero attribute in the docs which will force the chart to show zero.  Their color page is broken so it took some trial and error to change the color, I tried a bunch of options before it changed.  

###Following the line break are my notes from the lecture.
---
Wednesday June 29th
Morning Notes

Quiz 7 do tonight, do quiz 8 tomorrow.  woo~

Final exam + entrance exam into 301 will be over the weekend, no take-backsies on that one, it’s a for realsies test.

Code Review for an hour woo~.  This coffee is not as effective as energy drink.  

display: none removes an element from the DOM entirely, and replaced it when you change it’s display mode.  visibility: hidden keeps the element in the dom and sets its opacity to 0.  So it’s still there on the page, still takes up space, /and can be interacted with by the user if there are buttons or other events there even though they can’t see it/.  

A good approach to this hiding and displaying of things is to create a “hidden” class that you can then apply to hide and show things, and attach other behavior properties you want to that class as well.  

While you’re making your chart data is a good place to also calc the % of clicks through.  

COMPLEXITY = is a way to measure the efficiency at which we solve problems.  IF we’re doing something a lot of times efficiency becomes important and reducing the complexity of our code becomes important (later later).

Brian’s UI & UX talk -
There’s some examples in today’s repo of interesting UIs.  Take a look at them.  The Seattle Times project is open source and you can see their whole repo.

Just because it looks awesome doesn’t mean it was difficult to do.  Once you understand the basics it’s all possible.

Parallax designs - background images where our content flows over the top.  

We (as an industry) are generally moving back towards more simple designs.  Sliders/carousels/moving bits that are fancy people tend to ignore and aren’t effective.  Simple, minimal designs are “in” right now and 

Brian built a simple flyout menu for todays demo, and built it in JS.  It’s much simpler in JQUERY but doing it in JS helps us get a good understanding of the underlying code.  

CSS gives us the transform property which is allowing us to rotate our MENU text 90 degrees left instead of having to work with spans for each letter or some other goofy workaround.  Menu text goes away and comes back.

position: relative usually gives us the mental picture idea that there’s probably an absolutely positioned element that lives inside of it.  

border-radius on the right side but not left, so it looks right.  cursor: pointer is hugely valuable and clues users into the possibility of interaction there.  There are other types you can use such as crosshair and custom images.  Don’t overuse these, but they do have cool use cases once in awhile.

CSS and UI is still an incremental process, break the complicated object apart into it’s lego pieces and build/tweak each one until it looks like you want it to look. 

350ms is about the right timing for transitions, and is the default timing for most animations.  You can change this of course, but be careful.  Faster makes your site look jerky, slower and your site feels unresponsive.  

Why isn’t the transition property on the .active property ?  You want the element to transition away from, and back to, it’s static shape.  

When you rotate text (or other things) you might have to use negative margins/padding to nudge the element into position.  You can control casing in CSS too with the text-transform property.

Making more generic functions can be valuable, example: 

function toggler(element, label, state) {
	do some stuff that toggles those things
}

This can be used for more than moving the menu, you can reuse it all over your page to switch classes/states (where you use a class to add and remove/modify classes on an element)

setTimeout(function() {
text.style.display = ‘block’
} 350);

This ^^ makes the MENU text not show up again until the animation (which takes 350ms) until folding up the menu is over.  This runs at 60fps and looks really good.

Users like animations used sparingly, they are excited when things move and look nice.  All the animations on a page should run at the same speed and look very similar so users can navigate menus without confusion.

Stick with the 350ms timing for now, try out others later (or not at all).  You want an animation that looks deliberate and implies that there isn’t a performance issue in the background affecting your site.

When we move into JQUERY we will be able to make these menus with a lot less code.  

When you’re working with animations a simple answer for a hover state is to invert the colors (adjusting for background).  This will give your button/object a neat transition that still works with the rest of your layout.

Again the transform timing goes on the element itself and not the “.active” hover or state, because you want the element to transition into the animation, and back away from it again.  If you only put it on the .active part it won’t transition back to it’s first state, will snap back instead.  

IMPORTANT NOTE HERE is that we’re using CSS to control the animations/properties we’re changing to and from, via applying/removing classes to/from an element in JS.  This way we keep our styles in CSS and just add/remove them using our JS.  

http://codepen.io/briannations/pen/dXvEoq
http://codepen.io/briannations/pen/oLZRKK

After break notes——

PERSISTENCE - is how we keep data around on le web.  When you request some data on the web (even just loading a page in the first place) it’s stored somewhere else and you retrieve it from persistent storage.

Browser local storage is the same object interaction process we use in requesting persistent data from a server.  We learn these fundamental techniques from our local storage and will then later build this out into storing and retrieving remote persistent data.  

localStorage.stuff <— lots of built in methods

Examples:

.clear() — clears local storage
.getItem(key) — grabs key value ( )
.setItem(key,data)  — sets key value
.removeItem(key) — clears key and value

Once set these keys become basically properties of the localStorage method.  So:

localStorage.setItem(‘bob’,’My name is bob’)

then

localStorage.bob

will print

“My name is bob”

Local Storage is hard limited to 5mb, you can’t get more.  You should use it to store strings and other simple objects like arrays (after converting to strings), no images or other media because you’ll almost immediately run out of room.  

The Resources view of the Chrome developer console only updates when you refresh it, it is not a live view like the console is.  

We can access localStorage with either DOT notation or the .getItem() method.  

You can create items in localStorage via DOT notation too.  So:

localStorage.nick = ‘Awesome!’ <— will set this value

Whatever goes into .bob or .nick is always a string.  

JSON is the ‘standard’ type of converting other data types into strings for local (or other?) storage purposes.

JSON = JavaScript Object Notation

{ key : value }

{ “key” : “value” }

“{ key : value }” <— is how the entire object looks in the console if you inspect the whole pair

XML is the other/alternate method for data storage around the web (and it sucks).  Most people have converted to JSON these days I guess.  JSON is very much a standard method for moving data around the web these days.

JSON.parse and JSON.stringify are going to be our go-to methods to poke JSON and get the candy.

so our work path looks like:

We have an object we want to store (say an array) called derek that contains some object details.

var derekStringy = JSON.stringify(derek)

localStorage.thatGuy = derekStringy;  <—  the derekStringy object is now stored in local storage, after being converted to a string

if we want him back now:

var retrievedDerek = localStorage.thatGuy

we now have our stringy version of the derek object back, but it’s still a string and not an object.  

var parsedDerek = JSON.parse(retreivedDerek);

parsedDerek is now an object again, and the properties have arrived intact from local storage.  woo!  That was quite a trip I went on.

Two things to keep in mind —

Methods will not survive the stringify -> store -> retrieve -> parse journey.  They will fall off but the rest of the object will survive the trip.  

The INHERITANCE of an object is also stripped away.  It will be stored in it’s current state, but when it’s unstringified it loses it’s origin.  

You can concatenate lots of these commands together:

localStorage.dereksWheels = JSON.stringify(derek.cars) <— assuming derek.cars is an array with some of my cars

var rides = JSON.parse(localStorage.dereksWheels)  <—  parses that array back out of local storage and stores it in a variable all in one operation

We want to update our local data whenever it changes.  Don’t wait until later, you might lose data.

We only need to pull FROM local storage on page load.  We’re going to test if local storage exists then retrieve it.  If not, continue, and save new local storage as data is gathered.  

Local Storage is specific to a certain browser.  If you have multiple browsers installed they each have separate, persistent local storages of their own.  

An example of this in use:  apply a conditional for a newsletter that stores if you’ve seen it once.  Once you’ve seen it, don’t show it again.  This allows you to set one-time prompts for things.  