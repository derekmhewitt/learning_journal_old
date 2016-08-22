#Code 201, Day 5 Learning Journal
###Friday June 17, 2016

OK so it's learning journal time.  Bam!  Friday was a pretty good day.  My commute went much better, I think I've found a good location to catch the bus at down here.  Morning went well, I took the notes you can see below and I'll keep putting these in my journal entries as long as there's something to take notes on in class.  There probably always will be.  

The lab assignment went really well, I was able to do the branching part without any issues and the problems themselves weren't too challenging, but weren't easy either.  I spent some time trying to help another classmate whose name I can't remember now, I'm horrible with names.  Anyway I didn't want to just give him the answer, hopefully he figured it out this weekend.  He was stuck on question 4, where you have to reference the array location of the answer inside the output array.  

So since then I've been working on the readings, there was a lot of important stuff in the second part of chapter 3 of our JS book.  Objects, object constructors, methods, etc.  I think I've got an ok grasp on what's in there but don't quote me haha.  I'll read ch 5 of the JS book tomorrow morning on the bus so it's fresh in my memory for class.  My iPad also arrived so it'll be much easier to do my reading on the bus, no more trying to read a full page pdf file on my phone.  

Anyway I'm going to go work on the css on my about me page a little more and then put it up and turn that assignment in.  Then I just have the CSS demo to do for Brian, though there isn't an assignment for that (at least I don't see one).  Anyway hopefully that doesn't take too long to puzzle my way though.

###Following the line break are my notes from the lecture.
---

Friday June 17th
Morning Notes

We’re going to cover git branching today, wood~

We’re going over the quiz.  I hated that “avoid no white space” answer, it threw me a couple of times.  - At the very least try to use white space consistently in your own code, better practice would be to use it according to readability conventions.

Brian - Minifying and obfuscating code is typically an automated process post-development and pre-going live.  You should write your code in a way that it’s human readable and easy to debug, let the automated solutions obfuscate for you.  
The minifying process also removes whitespace and shortens variable lengths that reduce file size and increase the performance of your code.  

Unexpected token errors like the “}” usually come from not having the “{“ opening brace.  Other unexpected token errors generally have similar causes.  

Moving on to Code Review and CSS

Functions should be written as small as possible and only do one thing, and be named specifically for what they do.  You can use multiple functions together in order to do more complex things.
Prompts are an interesting scenario but we’re very rarely going to use them in real code.
Conditionals are the basis of most things you’re going to do in programming.  
console.log is extremely useful in terms of debugging.  Don’t ever try to figure out the result of something by assuming you’re correct, log it and read the logs.  

Variable scope - local and global.  
The reason we use var declarations is because of modules, a var declaration stays inside the module it’s coded in and doesn’t transfer to other modules.  If you don’t use var the variable becomes global in scope and can pass between modules?  This means if you or anyone else used that name outside of the module you’re working on it will do wonky things over there.  Re-assigning values for variables after they’re declared is perfectly fine and it’s an important distinction.

DRY code is important - Do Not Repeat (yourself, or your code).  A good example of DRY code is putting the increment++ counter at the beginning or end of a larger loop instead of having it inside of each of the smaller if statements.

calling a function also === invoking it
you call a function by: myFunction(); where () contains any arguments you’re passing into the function.  See yesterdays notes if needed.

General js structure for js files:

declare vars (global)

declare functions

invoke(call) functions at the bottom - they are the same.  Nick says call is used in Python pretty exclusively, rip Invoker QQW R

Wrapper - containing some code inside another layer which condenses it’s functionality into that single layer IE: a function (or method)

Divs are OKAY - BUT they are not to be used all over the place.  Usually we can be more semantic about things, using < section> and < article> tags to divide up your page.

when declaring classes in html you can put as many classes in between the “ and “ as you want.  Example:

< div class”classOne” “classTwo” “classThree”>
< / div>

HTML indenting conventions differ but generally if you have a child element, it goes 1 indent deeper than the parent.  If you have siblings they should stay on the same level together even if one is a heading or whatever.  Siblings stick together.

Every visual layer on your site is controlled through CSS, don’t use headings for big sized text.  You can modify any bit of text you want via class or id using css, don’t use a heading for that purpose.  You should use headings for important titles or headings in your site.
Only ONE h1 tag per page for SEO (Search Engine Optomization) purposes.  

Brian - Before you submit your code go through it and clean it up so that your output complies to regular standard practices.
Refactoring = restructuring your code, with the goal of making it simpler.  
When you look at an HTML site especially it should be easy to visualize the basic structure of your site just from the indent levels and use of structural html5 elements in your code.  
You should use comments sparingly and appropriately, they should say something specific without being overly verbose.  For now big comments are ok and it’s fine to write big comments if it’s part of our learning or development process, but cut them out of the final product and use just the smaller ones.  
Brian is a huge fan of classes for HTML elements that you want to style because you might need to use them more than once.  ID’s are just for ONE thing, classes can be reused as much as you want.  


Code Review of CSS
Base styles - wildcard for font family, body background color or other basic body mods, all right at the top.  

DRY is important in css, use multiple selectors at a time

div, h1, body, html, p {
	padding: 0px;
	margin: 0px;
}

Apparently the padding and margin properties might be a bad example because they will naturally cascade from body -> on down the tree but broadly speaking if you want to apply styles to a bunch of stuff use a combination declaration like this.

Be careful with your spacing!

div.page-section {
	some css stuff here
}

This says any div with a class of .page-section.

div .page-section {
	some css here
}

This says any child of a div with a class of .page-section gets “some css here” applied to it/them.  

Structure your CSS generally so that you begin with less specific things (*, body, section etc) and move to more specific as you go down the page.  

Most important CSS Selectors:


inline style	- overrides anything else.  Don’t do this ever or puppies will cry.
.# 			- ID
. 			- Class
< p>			- element
*			- wildcard - least specific element (well, it selects ALL elements)

These go from most specific from the top to least at the bottom.  There’s obviously lots of other stuff in the middle

Don’t put “!important” flags into css, it breaks stuff and overrides all other styles, is even more specific than inline?  I’m not 100% on that but it takes priority over (almost?) everything else.  Figure out why your styles aren’t working, don’t just throw an !important tag on there to get shit to work temporarily.  

If you’re going to use RGBA colors don’t apply opacity to the text, be specific about what you want - you want the background to be transparent but the text to still be readable.  



Friday Note #2

Outline: 
-	Fixed Positioning
-	Floats
-	Fixed Demo
-	Floats Demo
-	Layout Workshop Part 1

First two things: 
Everything on a website is a box.  Don’t forget it.  
w3schools and it’s usage is handy for learning the barebones fundamentals but gets a lot of more nuanced shit wrong and we’ll move to Mozilla documentation later because it’s more verbose and precise.  Also up to date.  You’ll know when you outgrow w3schools because you need more information than they provide.  

The more you know, the more you’re worth in employment terms.  If you want the $$ put in the effort because it’s worth it later.  As technology becomes more advanced and you’re doing things that other people can’t do, you’re worth more money.  
One thing Brian has a bunch of experience with is salary negotiations and personal branding, so pick his brain and ask him questions to help position yourself in the market.  

Box model discussion
Margin > Border > Padding > Content, where content is your HTML elements.  
Margin moves the box around, padding balloons the box.  Base value of all of these is zero px so they aren’t there until you put them there.  If the page appears to have to have these the browser is going to have default styles, so we’ll use a reset style sheet later in order to start with a fresh slate.  Rule of thumb: don’t do anything else until you Reset first because the defaults will be different between browsers and you won’t have full control of how your site will look if you build in chrome and they view in safari (for instance).

Fixed Positioning
Might have to link the video here because he’s going to draw on the board a bunch.  

Header = position of Fixed.  That means it stays at the top of the page and the rest of the page scrolls under it (if we give it proper effects?)  Width of 100% and a top: 0 value.  Ads and social media icons are often displayed using fixed positioning as well.  
How do we create something with a fixed position?

We can use Top, Right, Bottom and Left in conjunction with fixed positioning.  Why does my header do weird things?  Because fixed positioning removes it from the flow of the page and now we can position it relative to it’s first relative container.  If you don’t set any of the parents to relative it unattaches completely and floats in the top left of the homepage.  The element in question still inherits styles from it’s parents even though it’s no longer in it’s traditional page flow.  

Using the chrome dev console select an element and you can modify it’s style completely independently from the rest of the page using element.style (which is actually javascript? o.0)  Anyway this lets us poke our css live in the browser for every element individually.

Z-index is a pain to deal with because it cascades down from the body so it can be obnoxious to work with.  In the demo we gave github a fixed top header by fixing it’s header and giving it a z-index of 1.  BUT it removed the space of the header from the dom!? (flow?) of the page so we had to go back and push the content back into the place it otherwise would have been so that the content on the top of the homepage wasn’t hidden behind the new fixed position bar.

Floats~~~~~~
wooooo

Once you get fixed positioning down it’s no longer a challenge and you won’t have to struggle with it again.  

No one really knows how floats work aaaaaaaaa.  So Brian is here to tell us how Floats work, so we actually understand why they behave the way that they do.

Floats were originally created in order to flow text around something else (like a picture or other structural box).

Developers adapted floats in order to put boxes next to boxes, which isn’t really what they’re made for.  In order to get 3 boxes to float next to each other you’re removing them from the flow of the dom (page flow) and it does wonky things.

[ ]  [ ]  [ ]

^ three floating boxes (floating here = have a float value of left in CSS)

The first box is actually starting at it’s top left corner, and so is the second and third boxes.  Each time you apply the float to the next element you get the retained space back.  

The problem becomes not the 3 boxes themselves, it’s the trailing elements that do wonky things.  It’s going to begin at the top left corner of box 1, just like the 2 that are floating next to box 1 on it’s right side.

You can use the clear: left;  (or other direction, or both) attribute on it in order to fix a lot of these problems.  

Make a class called “clear_fix” and just put it’s only attribute as “clear: both;” on it so that you can quickly apply this around your page as necessary.  

http://www.w3schools.com/cssref/pr_class_clear.asp

Clear 

CSS will never be a cut-and-dry technology because of how it works.  Differences in browsers, screen sizes, etc etc all cause problems.  

The Fixed and Float demos and the workshop will be put out over slack and we’ll do them over the weekend.  


New Topic:
Git Branching

basic workflow: modify some stuff, A-C-P (Add, Commit, Push)

The master branch is often used for or directly represents a live deployment of your code.  So we use branches to take a snapshot of the current state of the product so we can work on it on the side building new content or features and then later merge it back into the master branch.  

commands:

git checkout branch-name-here			- this moves you into a branch that’s already created and moves you in there

git branch branch-name-here			- creates a new branch named branch-name-here

git checkout -b branch-name-here		- creates a new branch named branch-name-here and moves you into it

git branch 						- shows the different branches that live in your repo

View the slides for this presentation: https://github.com/codefellows/seattle-201d8/blob/master/class-05-images-color-text/5-git-branching.pdf

All these commands and the rest of them are in there, so you can look back and see the goodness that is slides woooo~

Your Master copy is always public facing and should never be broken.  

When you make a new repo always do an initial commit before branching.  If you don’t you will lose your Master branch and have ~issues~.  



