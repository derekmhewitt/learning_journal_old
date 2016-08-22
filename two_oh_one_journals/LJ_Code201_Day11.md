#Code 201, Day 11 Learning Journal
###Monday June 27th, 2016

Yesterday morning went pretty well, we moved right along through our agenda and got a good overview of our project from Sam before moving into lab.  Lab was tough, I spent a lot of time getting stuck with something that wasn't working.  I stripped all the extra stuff out and just worked towards mvp after bashing face against monitor for a while and finally got the random number generator running late last night.  I'll work on getting caught up today (Tuesday morning).

I spent the bus ride this morning learning about chart.js which seems interesting.  There's really a lot you can do with that, but I'm sure it's not practical to 

I've been thinking a little bit about project ideas but it's hard to find anything I really want to do or make that falls into the scope of "I can get this done in 5 days with 3 people helping me".  What I might pitch is a real world web design where we just redo their site - my dad is a member of a couple of woodworking clubs and they could use a web redesign.  


###Following the line break are my notes from the lecture.
---

Monday June 27th 
Morning Notes

Going over our weekly agenda.  Wed will be project presentations, thursday we’ll set teams.  We’ll go over proj requs tomorrow so we can tailor our proposals to them.  

Very basic: minimum 4 pages, 2 of which take and process user input.  

Student surveys - it’d be great if we could submit survey comments as they come to us instead of just once a week, maybe I should start jotting notes down.  Case in point - when we’re given assignments it’d be great if they were posted (even empty) a little earlier so that we can plan a little more around our workload.  Readings would be nice if they had a bit more of a custom prompt and weren’t just “write some response to your reading”.  It’s hard to respond to such a generic prompt for the 20th time, just a little variation there would go a long way.  

Going to go over quizzes and then code review woo~

Hoisting - when the browser loads a JS file the function declaration is loaded into memory.  A function expression can’t be used until after it’s declared, but it takes less memory.  

That one question: using border {} with no px size input blows away the 5px width from the previous border-width declaration so you end up with the default of “medium” whatever size that is.

Code Review - first taste of persistent data, he stored the store objects in local memory on the current machine using JSON

Support scopes are important, when you’re starting to do a project for a client it’s critical to set scope and expectations properly.  Generally speaking we want to expressly support IE9 and up only, IE8 gets into to some old wonky stuff that we don’t want to deal with.

Break and then assignment + code demo

Busmall!  We’re about to find out what that is, woo~

Catalog for the backs of bus seats, similar to old school skymall catalogs.  We’re going to build a market analysis app that will help them choose products to put in their catalog.

Instructions are in the repo - image management will be important here.  The purpose is to show users 3 products and have them choose which of those they’d be most likely to purchase, then collect the results.  We’re not going to show responses to the users until 25 selections have been made.  

On your results having cumulative #’s will be part of it, along with stats like how many times the img was shown vs how often it was clicked, so clickthrough %.  Tracking these stats will be important.  We’ll be using local storage at first, we’ll get to remote storage in 301, it’s similar.  

Charts are tomorrow, today we’re just worried about getting the random images part built and displaying.  

Part of todays assignment is to write our own user stories, so that we consider the users needs and wants.  

DOM element.removeEventListener(); <—  going to use something like that to remove the click listeners for the images when it comes time to pull them.  Hide and show dom elements, the button for results will be hidden until the user has clicked 25 times per session.  The chart and persistent data parts are for tomorrow, just focus on getting the images part working today.  

Objects need, at a minimum, the following attributes: name, file path, views, clicks.  Other ones I’ll probably use are % clicked, 

As just a cool addon, what about image overlays?  that display product name  and price or something

You can assign event handlers to a larger containing element by assigning ids to each picture and one to the container.  I’ll link the codepen for this.

function handleContainer(event) {
	console.log(event.target.id);
}

http://codepen.io/samhamm/pen/GqWgNX

Click events bubble up the DOM tree so you can grab them with larger items.  

How to handle not displaying the first 3 pics again?  we’re going to not repeat the set again, so after the first 3 we need to track the last 3 we displayed and not pick those again.  Rather than track the objects themselves, we can probably more easily track their position in the array and exclude them based on our random # generator

Break down your workflow into bite sized chunks.  Stick tasks into a function.  Think carefully about names and use semantic names that make sense.  