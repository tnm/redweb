Redweb
-------

Redweb is a web interface to the Redis key-value store and server. It is written in Python, powered by the Bottle micro-framework. You can think of Redweb as something like phpMyAdmin, but for Redis (and written in Python, of course).

But Redweb is more than that, too. The source can be reused to create web applications that utilize Bottle and Redis. For example, you should be able to piece together code from Redweb and (with some additions) cook up a simple Twitter clone. So Redweb is sort of like a reversible jacket -- you get two neat things for the price of one. Well, for no price actually, as Redweb is MIT-licensed and wants to be forked.

The basic idea derives from my super-simple [RedBottle](http://github.com/tnm/redbottle/"RedBottle"),project.

Install and Run
---------------

Installation is simple. The only requirements are [Redis](http://code.google.com/p/redis/ "Redis"), [Bottle](http://github.com/defnull/bottle "Bottle"), and the Python interface for the Redis (the latter two are included here). For now, I recommend using the version of the [Python interface] (http://github.com/razmataz/redis-py "Python Interface")included here, for its style of string handling (the [main trunk](http://github.com/andymccurdy/redis-py/ "main trunk") of redis-py will soon have similar changes).

Make sure Bottle and redis-py are in in your PYTHONPATH.

Start your Redis server, and then:

`python redweb.py`

The interface will start on localhost. The Python codes lives in redweb.py, and the web template code is at central.tpl. I've included some client-side form validation, as well.  

What You Can Do
---------------

You will be able to add key-value pairs, return random values, append lists and sets, and more, through an easy-to-use web interface. The code is easily portable, and can be incorporated into simple, quick apps that utilize Bottle and Redis.

More and To Do
---------------

Redweb is certainly alpha. It implements a fair amount of Redis functionality, but there is still more to be added. A soon-to-happen commit will implement union and intersection functionality. My plan is to eventually include all Redis functionality.

I intend to keep Redweb as current as possible for each new Redis releases.

Feel free to fork. Contributions are welcome.

Author: Ted Nyman - @tnm8

MIT License
------------
Copyright (c) 2010 Ted Nyman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

