#format rst

"Matlab makes it easier for beginners; but once you hit the wall, you hit it very hard |:)| I am using scipy for a few months now, after several years of matlab which I consider myself at least moderately knowledgeable about, and there is no coming back for me. After 2 weeks, I was more or less as efficient in numpy as I was in Matlab"

  *David Cournapeau*

-------------------------



"My real peeve is that Matlab is incomplete (batteries NOT included).  I'm "visiting faculty" (hired help - I've retired, but I'm teaching a course).  There came a point where we needed to solve a small set of simultaneous nonlinear equations.  The students here are required to have Matlab, so I said, "Just call up fsolve."  Oops.  In Matlab, that's not in the student version.  They'd have to buy the "optimization toolbox" to get it.  EVERY other math system has it ... but it costs extra in Matlab.

I wasn't fond of Matlab before that, but that little incident really soured me on it."

  *John Hassler*

-------------------------



"I was a huge matlab user for almost a decade; I tried to write a book about matlab (see http://matplotlib.sf.net/matlab_cookbook.pdf , unfortunately as incomplete as the mpl cookbook and other documentation).  At some point I "hit the wall" and could no longer be productive in matlab.  The extra overhead of managing complex data structures, developing complex GUIs, and working with networked data and databases was consuming most of my programming energy.  Yes, matlab provides you a simple, comprehensive interface, and a fairly complete set of numerical libs, but when you want to work with complex data in a realistic networked environment, you hit the limits of the language and environment pretty hard.  Then you rewrite what you like about matlab in python and get on with it.

matlab is a great tool for beginners and intermediates.  For experts, it has limitations which are hard to overcome. My advice to students: if you aspire to be an expert, bite the bullet now and build a set of tools that can scale with you on your ascent.  Also, realize that The Mathworks is like the crack dealer on the street: the first hit is free; once you are addicted it becomes quite expensive.  An academic license or a student version sells for under $100.  If you are a business and need the important toolkits, you are looking at 50K per year.  If you are an entrepreneurial student and dream of starting your own business once you graduate, ask yourself what you could do with the extra cash saved from a single site license.  If your fledgling business grows, ask yourself what you can do with the cash saved from 50 site licenses (hint, that is 2.5 million dollars a year). If you are ready to spend the 2.5 million dollars, fine, but first try the following exercises in matlab and python

* download and parse a CSV file from a web server, eg

`http://ichart.finance.yahoo.com/table.csv?s=INTC&d=8&e=29&f=2006&g=d&a=6&b=9&c=1986&ignore=.csv`_

  (for a python implementation, see the matplotlib.finance module)

* fill out a web CGI form in matlab (hint: you can do it with the

    embedded JVM, a virtual machine running in a virtual machine)

* query a mysql database on linux, win32, and OS X with the same

    script and populate an array with the results

Now how much would you pay? "

  *John Hunter*

