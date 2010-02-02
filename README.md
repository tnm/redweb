Redweb
-------

Redweb is a web interface to the Redis key-value store and server. It is written in Python, and is built on the Bottle micro-framework. With Redweb, you can easily interact with the Redis database through your web browser, utilizing POST functionality.

But Redweb is more than that, too. The Redweb source can be reused to create neat web applications that utilize Bottle and Redis. So Redweb is sort of like a reversible jacket -- you get two nice features for the price of one. Well, you get it for no price actually -- Redweb is MIT-licensed.

The basic idea derives from my super-simple [RedBottle](http://github.com/tnm/redbottle/"RedBottle") project.

Install and Run
---------------

Installation is simple. The only requirements are [Redis](http://code.google.com/p/redis/ "Redis"), [Bottle](http://github.com/defnull/bottle "Bottle"), and the Python interface for Redis (the latter two are included here). For now, I recommend using the version of the [Python interface] (http://github.com/razmataz/redis-py "Python Interface") (as modified by razmataz) included here, for its style of string handling (the [main trunk](http://github.com/andymccurdy/redis-py/ "main trunk") of redis-py will soon include similar changes).

Make sure Bottle and redis-py are in your PYTHONPATH.

Start your Redis server, head to the Redweb directory, and then:

`python redweb.py`

The web interface will start on localhost, so point your browser to **http://127.0.0.1:8080/**. 

The Python codes lives at ** redweb.py**, and the web template code is at **central.tpl**. I've included some client-side JS form validation, as well.  

What You Can Do
---------------

You will be able to add key-value pairs, return random values, append lists and sets, and more, through an easy-to-use web interface. The code is easily portable, and can be incorporated into simple, quick applications that utilize Bottle and Redis.

More and To Do
---------------

Redweb is certainly alpha. It implements a fair amount of Redis functionality, but there is still more to be added. A soon-to-happen commit will bring union and intersection functionality. My plan is to eventually include all Redis functionality.

I intend to keep Redweb as current as possible for each new Redis release.

Feel free to fork. Patches are welcome.

Author: Ted Nyman - @tnm8

MIT License
------------
Copyright (c) 2010 Ted Nyman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

