#Code 201, Day 3 Learning Journal
###Wednesday June 15, 2016

This morning we went over the days agenda and did our first code review.  

We worked on initializing a local repo and getting it synched up to github that way, which was a little bumpy.  I helped a couple of other classmates with theirs and it seemed like we got everyone caught up with it after lunch.  

The lab assignment for today wasn't difficult, but I made it difficult.  First of all I didn't think through the logic of the problem before I started writing any code.  I don't think you need every detail tied up before you write your first line, it's ok to wing variable names sometimes.  But I ended up with both question 6 and 7 being not as good as I'd have liked.  After struggling with question 7 for a while I finally just commented out my error correction because I could not get it to work properly.  Which was also actually a good lesson for me - sometimes a product just has to be shipped, even if it's not perfect.  And the code I wrote, even with that block commented out, did more than meet the MVP standards we were shooting for.  Your code can always be better, and even after it's shipped version 1.0 there's always 1.01 to iterate on the next issue you're having.  

So just a funny point that came up copying my notes in here, apparently a < script > tag will break mou and maybe the .md format all together if you don't close the tag?  Mou really doesn't like it anyway.  

###Following the line break are my notes from the lecture.
---

Wednesday June 15th
9am Notes

Best way to tweak CSS without dealing with lots of little popup boxes is to comment out the < script> tag in your html (temporarily).  

Quiz 1 will be pushed out later today, we’ll have a full day to do it.  

Code Review - 

What’s the deal?  There’s a lot of good articles you can look up to see that it’s important to share code and ideas.  There’s lots and lots of good reasons why you should review code, do some self reading on it.  

Lots of goofing around with Git and we’ve now got our learning journal repo initialized locally and connected up to github.

Moving on after break~

From the JS book

Statements and Expressions

JS is basically a series of instructions.  First you do this, then the next thing, etc.  Each of those instructions is a statement.  Statements should end with a semicolon.  

The reality is that missing semicolons often will not break your code in real world applications.  Modern browsers have a feature called ASI - automatic semicolon insertion.  They give your code a quick read through before executing it the first time and check it for these errors.

Expressions
An expression evaluates into or results in a single value.  Broadly speaking there are two type of expressions:
expressions that just assign a value to a variable, and expressions that use two or more values (or variables) to return a single value.  

Comments - you can have single line comments, comments after code, and multi-line comments if you want.  
You cannot stop a comment mid line and start coding, it isn’t allowed.

Variables
Where and how we declare variables will be important to us later.  If you have a variable and where you declare it is going to affect the way that it works.  The keyword ‘var’ declares a variable and new variables do not need to be declared with a value or data type (in javascript anyway).  

You can’t start javascript variables with a number.  You shouldn’t start them with $ or _ either, but it is technically possible.  There will be reasons later why we might want to, but for now just don’t.  Start variable names with a lowercase letter.

You cannot use a - or a . in a variable name.  The - is a minus sign, arithmetic operator and . is part of (dot) notation.  You can use _ and $ but we should stick w/ camelCase for now.

You can’t use key words or reserved words.  They’re the words that do things and have specific meaning, they are protected by their status from our reuse.  For instance you can’t declare a var called var, it’ll throw an error.  

Javascript is case sensitive, so score and Score would be two different variables.  Don’t do this, it’ll just make your life difficult.  Use completely different variable names.  

Revisiting arrays
Arrays store a list of values, or a set, group, whatever.  The values (or strings, or booleans) inside an array are called elements.  The way JS works in an array is that each one is numbered, the first one is element 0, second is element 1, etc.  So to get the second element use array[1].  The real key to using arrays is remembering that inside the array all the elements are related to each other.  Objects are used to gather up dissimilar information, arrays should get the similar stuff.

example:
var team = [‘sam’, ‘brain’, ‘nick’, ‘nadia’];

You could make:
var dissimilarCrap = [3, false, 17, true, ‘derek’, -7];

But that’s not a very good use case for an array, these things don’t have anything to do with each other, and using the array would be difficult.  The only possible use I can think of is to maybe do error or log collection and put it all in one spot to then print it out to the console or log it all to a file at once.

To access a nested array (and array inside another one) you use a 2nd set of brackets.

Example:

var myArray1 = [12, 37, 14];
var myArray2 = (23, 87, myArray1];

so using myArray2[2][1] will result in the value 37.

you can assign a new value to myArray1 by:

myArray1[3] = X; where X is a new value.  If you had a position 4 you would overwrite it with this provess, but since we don’t it would create a position 4.  

If you mess up and use the wrong # inside the boxes (where [3] is in the last example) you will have undefined values in the middle of your array.  This might be fine sometimes, but is probably not desirable.  

Loops
for (some condition here){
do these things;
}

syntax looks like:
for (starting # ; max #; increment counter)

To establish a starting # we declare a starting variable, usually i but you can use other variables and even external variables as long as you have a specific purpose for doing so.  “team” is an array from our example above.  
for (var i = 0; i < team.length; i++){
console.log(team[i]);
}

undefined
when you have a code statement like the above for loop at the end the console will give you an undefined “error” that’s not really an error because even though your code is no returning a value, it’s doing what you told it to do.

parseInt()
Takes a string and turns it into a number.  When you accept input from a user with a prompt dialog you get a string, so using parseInt() around that prompt will parse the input into a numeric value on the same line so that you can compare it to numbers directly or use it with arithmetic operators.  

Lab stuff
- add a 6th question where the user guesses a number and gets 4 tries
    - decision tree for options, user gets 4 tries (3 additional) if they’re wrong
- add a 7th question where the users has to guess the answer to a question and the possible answers are in an array.  They get 6 tries to guess the answer, show them the possible right answers at the end.  You’ll need a for loop to test the users answer against the array.  


Lab Notes

Working off yesterday’s About Me project, here’s what I need to add today:

- For new questions add console.log statements
- Add ordered or unordered lists
- Make the page interesting and fun?  add css and style
- (done) Add a Top Ten list to the bottom of my about me page, ordered list, can be any top 10 things.
- keep your top 5 questions

- add question 6: takes numeric input by prompting user for a number, indicates to the user whether the guess is “too high” or “too low” and gives the user exactly 4 attempts to get the right answer.  

- 7th question: multiple possible correct answers stored in an array.  Give the user 6 tries to guess the answer, if they get it right congratulate them, otherwise the game is over.  Either way at the end display a list of the possible correct answers (write the array to an alert).

- Keep track of the number of correct answers and tell the user how many they got right at the end, and address them by name (already done).  

Stretch Goal - 

User Stories (Stretch goals... not required!)
* As a developer, I want to make my code more DRY by putting all of the questions, answers, and responses to the first five yes/no questions in my guessing game into arrays (or even one huge multidimensional array), and modifying the game logic such that a 'for' loop will control the flow from question to question. (This will take some planning... here's a hint on how to approach it!)
for (var i = 0; i < numberOfQuestions; i++) {
  var answer = prompt(questions[i]);
  if (answer === correctAns[i]) {
    alert(response[i][0] + userName + response[i][1]);
  } else...



