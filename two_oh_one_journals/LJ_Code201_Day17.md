#Code 201, Day 17 Learning Journal
###Wednesday July 6th, 2016

Our standup meeting this morning went pretty smoothly, and actually the morning did too.  Liz and I pair programmed together and we wrote quite a bit of code handling the selection of the elements inside the click handlers, the determinations between correct and incorrect answers, allowing only one answer per ul to be selected at a time...  probably some other ones I'm forgetting.  We also set things up so correct answers move down to their own ULs below the matching game.  We still have one 'bug' in the functionality on that page where it's possible to select the ul itself using the click handler, I think it'll be solved with an if statement tomorrow where IF the click (event.target) is a ul there's simply no action taken, and the only 'else' option available is a li element.  Or maybe just IF the target IS an LI THEN ...do stuff, otherwise just ignore the click.  Either way works.  

This afternoon we hooked up to the projector and viewed our project over there, which was nice.  We talked through the design as a group of 4 and wrote down tasks that are in github issues for each page, so we've got a good working task list for tomorrow.  I added sound to our flashcards on learn.html which went a lot more smoothly/easily than I expected, they're nicely embedded and the audio element handles switching src="" very smoothly.  

The animations for test.html/test.js still need some work, I got the elements selecting smoothly with a transition timer but their movement down to the lower set of answer uls is still instant and I feel like it's a little jarring.  We'll see if we can come up with a better solution along with further styling for the page tomorrow.  

And that's about it.  Liz and I worked very well together, I think she was a good partner.  Several times she caught me on a minor spelling error or other typo that would have led to some fun bug chasing but didn't because of a second pair of eyes.  She was also very helpful to talk through ideas with, clarifying what I wanted the code to do to her helped me think through the problem and the code was easier to write because of it.    

###No lecture notes today.
---