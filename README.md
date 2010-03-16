Redweb
-------

Redweb is a web interface to the **Redis key-value store and server**. It is written in Python, and is built on the Bottle micro-framework. With Redweb, you can easily interact with the Redis database through your web browser, utilizing POST functionality.

But Redweb is more than that, too. The Redweb source can be reused to create neat web applications that utilize Bottle and Redis. So Redweb is sort of like a reversible jacket -- you get two nice features for the price of one. Well, you get it for no price actually -- Redweb is MIT-licensed.

The basic idea derives from my super-simple [RedBottle](http://github.com/tnm/redbottle/"RedBottle") project.

Install and Run
---------------

Installation is simple. The only requirements are [Redis](http://code.google.com/p/redis/ "Redis"), [Bottle](http://github.com/defnull/bottle "Bottle"), and the Python interface for Redis [redis-py](http://github.com/andymccurdy/redis-py "redis-py") (the latter two are included here). The version of redis-py included here is the newly refactored one -- Redweb is designed for this new version, and it is highly recommended that you install the new client.

Make sure Bottle and redis-py are in your PYTHONPATH.

Start your Redis server, head to the Redweb directory, and then:

`python redweb.py`

The web interface will start on localhost, so point your browser to `http://127.0.0.1:8080/`. 

The Python code lives at ** redweb.py**, and the web template is at **/views/central.tpl**. I've included some client-side JS form validation, as well.  

What You Can Do
---------------

You will be able to add key-value pairs, return random values, append lists and sets, return and store intersection and union for sets, and a good deal more -- through an easy-to-use web interface. You can also use standard Redis syntax to search for keys, and you can delete keys.

The code is easily portable, and can be incorporated into simple, quick applications that utilize Bottle and Redis.

More and To Do
---------------

Redweb implements nearly all current-release Redis functionality, but there is still a bit more to be added. 

Redweb will be kept current with each new Redis release, with each update documented. 

JSON serialization is also on the to-do list

A [blog post](http://philosophyofweb.com/2010/02/redweb-a-web-interface-for-redis/ "blog post") about Redweb, with screenshots.

Feel free to fork. Patches are welcome.

Author: Ted Nyman - @tnm8

Screenshot
-----------
![Screenshot of Redweb](http://www.philosophyofweb.com/redweb5.gif "Redweb")


MIT License
------------
Copyright (c) 2010 Ted Nyman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

