#Code 201, Day 18 Learning Journal
###Thursday July 7th, 2016

Thursday..  was a day.  We made a lot of progress but it was stressful.

New stuff:

The css property overflow: hidden will make you hate your life if you're trying to get absolutely positioned elements to show up.  I know this because I spent about 30min this evening trying to fix our header, so that the h1 and nav elements would be positioned relative to the header_inner class'd div instead of to the browser window themselves.  

Another new thing was getting html elements that are appendChild'ed to another to animate and fade in.  This code accomplishes that:

'''
    matchingLeftNodes[0].style.opacity = 0;
    matchingRightNodes[0].style.opacity = 0;
    correctLeft.appendChild(matchingLeftNodes[0]);
    var correctLeftNodes = document.getElementById('correct_left').childNodes;
    window.getComputedStyle(correctLeftNodes[4]).opacity;
    correctRight.appendChild(matchingRightNodes[0]);
    var correctRightNodes = document.getElementById('correct_right').childNodes;
    window.getComputedStyle(correctRightNodes[4]).opacity;
    correctLeftNodes[4].style.opacity = 1;
    correctRightNodes[4].style.opacity = 1;
'''

For some reason ''' and ~~~~ aren't working to make code blocks.  Welp.  

And that's a snippet from some of the code that I wrote today.  I seem to have lost the site where I found the technique or I'd link it for future reference, because he listed a couple of other ways to accomplish the same thing using jquery.

Anyway Liz and I stayed late today and chased little bugs/annoyances that were hanging on and I think we're in good shape to present tomorrow.  Woo!

###No lecture notes today.
---