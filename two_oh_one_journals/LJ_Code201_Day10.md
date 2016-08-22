#Code 201, Day 10 Learning Journal
###Friday June 24th, 2016

Friday's lecture went pretty well, though I feel like we got a little sidetracked with the git discussion.

Lab went ok but took a while to get rolling, working with a group of 3 is really challenging.  Just trying to figure out what we should do first with 3 people is much harder than two.  Anyway we got it rolling and worked on the lab over the weekend, it took a couple extra hours to get everything looking like it should.  Those little round circles and the underline bits were both kind of obnoxious to do, but I think I got a pretty good copy of them.  I found a codepen (which I sited in the readme) with some pretty good instructions for making something like that:

http://codepen.io/graygilmore/pen/39bda748ab009f4ae285cbcbe73772b9/

Which helped a lot, from there it was possible to just play with the sizes and get it looking how I wanted it to look.  For CSS I'm starting to do more of what Brian has been talking about - I lay out the major stuff with whatever size seems good and then save, refresh in the dev console and then play with sizes right there live in the browser.  It's so much faster than switching back and forth.  The only trick is to go back and update your code regularly because it's super easy to forget what you've done and then you lose your changes because you can't remember what you changed.  


###Following the line break are my notes from the lecture.
---

Friday June 24th
Morning Notes

Image work is not inherently part of web design, or even more general design work, but design and web design have a lot of overlap.  GIMP is free, I’ve already got it.

Start thinking about projects!  What is a project I could do ?  Apparently games are really common.  Maybe a basic eve fitting tool that’s animated via css with drag-and-drop modules?

Code Review - we’re working on Erica’s JS, it’s broken and probably could be DRYer woo~

File management - 

CSS files go in a css directory, JS files go into a JS directory.  
Images go in images, media or assets (all name p much mean the same thing).  
If you have lots of base html files you can put those in an html directory too (pages maybe?).
If you have lots of html files and some are private you can have public vs private directories, where the private(company?) ones are behind a login prompt or something.  This gives a nice division to your organization so it’s easy to keep track of which pages are confidential while you’re working on them.

If you’re going to move assets around you have to update all of your pointers to those files to their new locations, so be careful not to break shit via this method.  

reset.css files should be in their own file and applied as a very early part of your workflow.  At the start of your project you should build an index.html and link your reset style sheet to your project, it’s just one of your first steps.  

Before you build anything in css you should have a reset style sheet before you do anything else, because the reset is going to wreck your work if you apply it later.  Everything that you visually see on your site is controlled through css.  

command line stuff:

less index.html will show you the file, and you hit q to quit
cat will do the same, but prints it into the terminal

Back to DRY code, we’re going to separate out the “create element, give it content, append it to the dom” part of our js into 1 function that we then call and pass arguments

function buildElement ( kind, content, where) {
	var x = doc.createEl(kind);
	x.textContent = content;
	where.appendChild(x);
	return x;					<— this will be used to then append a class, but otherwise is not necessary
}

The above type of function needs to be in the global space because we call it inside of lots of other contained functions.  If you tried to do it any other way you’d have to re-declare it a bunch of times and that would defeat the purpose.  

In javascript if you have a function that accepts 5 arguments but you only specify 3, the remaining two will be undefined.  That won’t break anything by itself, js doesn’t mind having undefined variables.  And (for instance) assigning a class of undefined to various objects will actually do nothing.  You could write that either way, with an IF there’s an argument there, THEN assign a class as part of your build element statement.  

Building table rows is also possible with the same function.  

This buildElement function is a great example of good code, it’s very modular and you can reuse it a lot in your code base.  

ABSTRACTION - almost everything we do in computer science is work within an abstraction layer.

Right now we’re working inside a LOT of abstraction layers all stacked on top of each other.  Processor -> processes -> operating system -> notepad/atom/web browser.  Obviously that’s oversimplified but it’s just an example.  


Brian’s CSS lecture -

UI vs UX - user interface vs user experience

ux is button placement and ease of navigation, clear navigation paths through the site, speed and optimization, etc

There are very important “standard” element to ux design that make it difficult to do crazy cool things with your ui.  

We’re in an era of minimalistic design with lots of whitespace or large blocked colors.  Just because something looks really cool doesn’t mean it was necessarily hard to build.  


Today we’re going to build out the bottom of our layout page from yesterday, and we’re going to do some CSS animations.  JS animations is another option too.  Getting the timing of the animation right is difficult, you want a nice responsive design but one that doesn’t feel jerky..  not too fast or so slow that your site feels slow and unresponsive.

Sometimes you can get some weird wonkiness where your site doesn’t fit 

overflow scroll or overflow auto - these will create scrollable text boxes.  Auto is based on your browser, scroll forces that scroll functionality.  You can style a scroll bar, but we shouldn’t do that.  Almost everything is possible, don’t stretch yourself so thin you can’t get there.  There’s a CAN you do something vs SHOULD you do something?  kind of space here.  However, if doing this creates more problems than it solves, or takes a silly amount of time/$$ to do, it’s probably not worth it.  

Deadlines never get met in software, but your goal should still be to get as close to on time as possible.  

Don’t get stuck in the developer bubble, it’s confining and you’re cutting yourself off from the business side of the business.  

html attribute tag < section role=“content”>    <— the role tag is just meta content and is not usable by js or css, it just provides information.

Working with extra containers can be useful in certain circumstances, like floating our picture next to our scrollable text box.  Floating the image left will also 

Our current website is a static, hardcoded site but we’ll have templates later that allow us to dynamically assign content into these spaces (like our scrollable content box).

Percentage based sizing units like % and em are great for responsive designs.  We’ll get into those in 301 more, for now you can try them out.  An EM is going to be in relation to the parent element, an REM is going to be in relation to (something else, I’ll look it up).  One EM is equal to a 16 pixel letter m in your browser window, so you can scale fonts really easily using this unit.

In relation to responsive design, pixels are fine.  Not everything needs to be % based, pixels work really well in a lot of situations.  Often fonts and other fixed assets like logos and pictures don’t need to scale, they look fine at static sizes.

Use clear: left or clear: both to make sure you’re sitting happily below floated elements.  If we interrupt the flow of the DOM we need to ‘restart’ that flow again with a cleared element.  

If you understand these principles well you’ll be able to build any layout you want to build:  
Display Types:  Block, Inline and Inline-Block
Positioning Properties: in particular Relative and Absolute positioning
The Box Model
How to work with floats and how to clear them

Using 50% + 50% + gutter can = to 100% ?  

Use width: calc(50% - 30px);

SCSS is a “new” version that allows us to do math, functions and loops inside your css.  It takes a lot of the functionality load off js.  We’ll talk about it towards the end of 301 and in java 401, which I probably won’t be going into.

the overflow: hidden, auto or scroll properties allow you to make text boxes scrollable.  You’ll usually use overflow: auto so that you only get bars if you need them.  Hidden is for articles you click on to then get more of that article.  line-height: 26px or whatever # can give the text inside your scrolling box some more definition.  

copy and pasting code from the chrome dev console into your code gives you the de-selected parts commented out automagically, which is really cool.

As soon as you start messing with text-shadows and box-shadows we’re bak to 1999 and you’re going to run into those old styles and perceptions of them affecting your work

Google Chrome dev console Tips:
- at the bottom of the dev console in the elements view the parent -> child relationships are defined at the bottom of the window on mouseover
- In the styles view, you can toggle the :hov attribute in order to turn on hover states on any element you’ve selected.  Now you can work and style the stuff in there, along with other hover-like states such as visited
- You can choose the speed of your animations, 350ms is the standard.  You can speed them up or slow them down
- The styles in the window that scrolls are in order of importance from the top down, so you’re going from most to least specific.  When you’ve overridden a style it’s going to get crossed out and something “above” it in the list is overriding your crossed out element.  
- The phone and extra device settings in the chrome dev console are just emulations and are not super accurate representations of those phones or tablets

Lab Stuff:
Create a webpage from a provided design comp.  We’re doing pair/triple groups so we’ll have to work together woo~

Class repo -> layouts page, there’s 3 pages there.  Each of us will make one of them, so groups of 2 will only make 2 of them.  We’re going to try to get our end product to look as close to the original as possible but using html elements and css instead of photoshop obviously :p.

Don’t forget your css resets, use a group repo to work from, instructions are in the readme.  Use placeholder images, can be any type (I hear cats are popular).
