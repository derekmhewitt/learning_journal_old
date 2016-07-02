#Code 201, Day 15 Learning Journal
###Friday July 1st, 2016

This morning started out with Sam's alphabet soup on the board.  I felt pretty good about that, I knew most of those acronyms already and had a good grasp of what they really mean.  The 401 intro talks were pretty good..  I was already pretty sold on Python and Nadia showing off her project drove that home.  I realize it's going to be a hard couple of months but it's probably worth it.  I'm seriously considering renting a room downtown here for the duration so I'm not stuck commuting several hours per day during that crunch.  Compared to the cost of the course it's not that much /more/ expensive to rent a place month-to-month, it's just about finding one nearby.  Anyway I'll keep looking.

The 301 presentations were alright..  I was a little bit underwhelmed?  I know a lot went into both of those projects and implementing the google maps API..  Maybe I'll just have to wait until I get there and can appreciate their scope a little better.

This afternoon's work on the project went pretty well, we got our proposal approved and moved into design work.  We've got sets of homework for the weekend and everyone has code to write or jobs to do, and they're not touching the same bits of code so we're (hopefully) not going to run into a lot of merge conflicts.  I'm going to try to get my work on the Learn page mostly done tomorrow so that Aziza can start coding the Test page based on my constructor and fake test objects.  

Hopefully we can come in on Tuesday and get caught up with a quick standup meeting, then get to work on new features quickly.  I feel pretty confident at this point though, there's nothing in this project that is a really big stretch or beyond our abilities, it's just using the skills we've learned to turn out a professional quality design and application.  



###Following the line break are my notes from the lecture.
---
Friday July 1st
Morning Notes

WYSIWYG - What You See Is What You Get

Make your own basic WYSIWYG editor?  HTML, CSS and JS combined project.  Going to be pretty heavy.

CMS - Content Management System
Facebook is a sort of content management system, wordpress is, twitter mostly is too.
Once we’re through 401 we’ll be capable of making our own CMS, capable full stack developer(s).

In fact there’s a CMS being built in this building about 200 feet away, for the new CodeFellows website.  The people who need to update and post content on that site don’t have to be devs, so we’re making our own CMS to get that stuff done.  

Quiz 8 is due tonight, 301 entrance exam goes up today and is due Monday Night.  



iOS Preview 
Adam - has a great beard.  He went through iOS himself and now is assistant instructor for the course.

Why is he here?  We have hard choices to make about where we want to go with our development career.

iOS is a design-centric development environment where they work primarily with mobile devices.  They teach multiple languages using cutting edge techs like Swift, MapKit, iBeacons, SocialFramework, etc.  
iOS has the best graduating avg salary of 401s available at CodeFellows, $79,727/year for post graduates.  They also teach objective C.

They build out lots of apps during their classes, including twitter and instagram clones.  Swift 3 is coming out shortly and is open source so it’ll be available there.  They release apps into the App Store directly (or try to anyway, don’t always get approved by Apple).

Swift is the most loved programming language(apparently some data supports this).  

Arguments for iOS
Swift is open source
Develop your OSX and iOS applications from the front end to the server side entirely in Swift

Google is considering using Swift to develop Android apps —  native Swift android apps?  Maybe?  

Swift is one of the fastest growing languages around and isn’t done growing yet woo~.  

Paul Haggerty 
iTunes U - Free Course available online though Stanford

ObjectiveC and Swift are very different in the job market.  Some of the larger companies don’t like Swift as much and are working in ObjectiveC.  But we teach both woo~.
iOS doesn’t teach you anything about developing for Android, that’s a separate subject and different language.  Unless Android opens up and supports Swift, which they are considering.  

Apple VR hasn’t really been confirmed / denied / is just a rumor at this point.  There’s no information so far about what language that might use either.




Code 301 Preview

Concepts:
- MVC
- Responsive Design
- SQL
- Single-Page Application Development
- Services and APIs
- Algorithms
- Functional Programming
- Relational Data
- AJAX
- APIs

Languages:
- Advanced HTML Templating
- Intermediate CSS and Intro SASS
- Intermediate JavaScript
- jQuery Events & DOM Manipulation


req/res cycle - request/response.  This is the basic cycle of communication between client and server.  

HTTP <— Hyper Text Transfer Protocol

REST <—  Representational State Transfer is a concept of transferring states or conditions.  This concept underpins HTTP and other APIs.  

View Layer <— Clients are often referred to as the view layer.

Controller <—  The Server

Model <— The data stack, referring to how we model and structure our data in code.  data.datasets[0].data[0]  from this week is an example of a data model.

MVC <—  The Model View Controller (out of order for some reason idgi) but this is the name for the overarching concept we’re discussing above, Think in terms of variables being the model part, the view layer being ‘front end’ like the html/css/js, and the controller is the ‘back end’ where the server lives.  The vars move through the server according to it’s rules, which are the API.  
Modular code structures, every little thing has it’s own little place and is decoupled from other stuff.  It helps with debugging and working in large code bases and groups of other coders on larger projects.

Responsive Design - SCSS (referred to as SASS) is about writing modular and reusable css using SASS which allows us to use lots of js type properties like variables in css

SQL - Relational Database Systems and how those work.  Document based storage.  Mongo is what you’re going to learn in 401 but is based on SQL.  SQL (pronounced “sequel”, stands for Structured Query Language) is still very widely used.

CRUD <— Create, Read, Update, Delete

Single-Page Application Development - Instead of having lots of different html “pages”/files we’re going to use an abstraction layer to reload into the browser new information and trick he browser into thinking it moved pages on the larger site.  

Services and APIs  <— get is an example

Dynamic Web Development woo~  This goes back to the Single-Page thing where you’re dynamically loading new content into the same browser without refreshing or “moving” pages.  

How does the full stack work?  How does the Internet work?  We’re going to learn basically the answers to those questions in 301, stacking concepts.

Functional Programming - methods (in particular array methods) we’re going to be using more complex jQuery I guess to move into an understanding of process that are abstraction layers.  Complicated huh?  It’s tough to learn this, but once we learn it they’ll be super helpful woo!

Relational Data - working with JSON a lot.  Most things have a JSON api where we can get data that comes back to us in a format we can understand and work with in JavaScript.

AJAX - Asynchronous JavaScript and HTML which allows us to send new data to the server, or get data from them in a response that the page loads, and then loads it into the page you’re currently already viewing.  Infinite scroll is a great example of this and is super powerful in use.  

Handlebars.js <— html templating.  Angular.js is very similar

Intermediate CSS and Intro SASS <—  You’ll probably almost never make a static site again.  You’ll be making responsive designs and SASS helps you do that.  This involves sites that respond to mobile screens and resize dynamically, stuff like that.

Intermediate JavaScript <— The ability to leverage the constructor pattern we’ve been working on so far, by stacking and wrapping various elements into modules.  We’re going to package these things up in order to load in what we need and exclude the modules we don’t need.  

jQuery Demo 
———
+ Accordion Menu CodePen Demo


Clicking on logos to go back to the homepage is one of those things we’re all accustomed to having on webpages, but it’s never really explicitly stated that that’s what is happening.  

JS 401 —>  Is extending 301 even further into advanced js for front end dev, and using Node.js for back end functionality.  

REPL  <— Read Evaluate Print Loop.  Your Console is an example, and the chrome dev console is another one.  JavaScript and Python REPLs are available, the Python one is installed on OSX by default.


Python 401 <—  Class Overview


You can actually detach element from the DOM, using the transition on the element itself it’ll animate.  You then attach them to the new UL in the results box.  Either Detach of Absolutely position them.  Outer box will get shorter over time w/ a transition on the box.  