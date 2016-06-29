#Code 201, Day 12 Learning Journal
###Tuesday June 28th, 2016
Lecture this morning was pretty good, Sam was on brains detail and I think he did a pretty good job helping us all catch up.  The handling of the random number generation part of the Bus Mall project is one of the trickier parts of it, the rest is mostly just plugging things together and figuring out which parts go where.  I got caught up to mvp today with the chart working and started styling the page with some basic colors and added fonts.  I'm not sure what else I'll do to it stylistically, maybe find a couple of pictures to stick in just to liven it up.  Oh and style the bar chart, maybe even do a couple of different chart types?  That's all possibly on the menu.

Anyway I'm generally feeling better about the whole project after yesterday, for some reason I got so stuck on that random # generator that I didn't make much other progress.  I know you mentioned this morning I had put classes instead of ids on some of my html elements, but I hadn't even noticed yet because I never got around to trying to hook them up to anything...  Anyway I'll try to remember that lesson in the future and not get so bound up in a small part of a larger project that I can't see the forest for the trees.


###Following the line break are my notes from the lecture.
---
Tuesday June 28th
Morning Notes

Passing of Pat Summitt - she was a women’t basketball coach and important figure in advancing women’s equality in sports?

We’re on brain detail today, and need to scoop up the brains from yesterday because we need that stuff working for today.  We’re going to build out today’s assignment and get to mvp this morning so we can move forward.  

Minimum standards for group final projects (there’s a big list but the major ones are):

- 2 pages must take user input
- user’s state must persist across multiple pages
- at least 3 interlinked pages, maybe more

Waffle.io - some kind of git management tool?  I’m not sure but look it up, might be helpful.

Final project details are published on Canvas now so we can read through the requirement at our leisure.  


splitString() is a method for splitting strings at a specific spot, such as the period in a string.  Nadia did her version of this project when she went through by splitting off the img/ in the front of the file path and the .jpg extension off the end, in order to just pass in 1 variable to the constructor function (which was the full path) and trim that down into the image name.  

The psychology of building these things and making small bits of progress is important.  Break problems into smaller pieces and tackle the as more bite sized pieces.  

We won’t be able to do the char.js portion of today’s lab at all until we’re tracking clicks and views on our images.

Ultimately what we’re going to do with this is kick our views + clicks out to a separate array and then run through them with a for loop to make our chart

In html there’s an element called canvas (which I hear is pretty awesome).  It’s where charting libraries put their output, games draw their environment, etc.  Most of what we do in canvas is 2D but you can draw 3D images there using openGL.  

In a script tag in your head you bring in the char.js library in order to use it in your project.  looks something like < script src=“ some source“> </script>

Our script code should still be loaded at the bottom of the body (the last line above/inside the closing </body> tag

Accessing data nested several levels deep inside complex objects is a process you need to think through carefully.  When in doubt throw it into the js console and try accessing it to see where you’re at.  

data.datasets[0].data —> is an empty array [] where your clicks go.  

You might want to make vars to hold the data from your item objects that you want to put into your chart.  You’ll run through those objects with a for loop and push that data into these arrays, which you then insert into the chart renderer.  

Keep focused, there’s lots of things in the docs.  All we need to do is put our data into the right spot in the chart code and it’ll render the chart we need for this project.  


As a more general statement about data handling, use some other tool to do your data analysis and use a js charting tool to display those results.  JS isn’t that good at math heavy interactions.  There’s a lot of libraries out there that are more plug-and-play, you insert the library you want to use and use the part of it you brought it in for.  Chart.js is a good learning tool but in general we’ll import a library, use a function it provides us and move on with the next thing.  

To style the colors on the chart bars you need to specify a color for each bar.  You can alternate back and forth but you have to put in as many colors as you have bars, there’s no automagical way to do it.  