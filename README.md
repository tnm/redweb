Redweb
=======

Redweb is a internal web administrative and query UI to the **Redis key-value store and server**. It is written in 
Python, and is built on the Bottle micro-framework. With Redweb, you can interact with Redis through your web 
browser. 

This is **not** a REST interface to Redis -- it is designed as a web interface -- and its internal structure reflects that.
URL's are mapped to Redis commands in an RPC-style, accepting keys and values as parameters. An example of REST-style 
interaction is something like another old project of mine, [diner](https://github.com/tnm/diner/), with the key 
identified as the resource.

The Redweb interface obviously should not be directly exposed to the Internet. 

Here's a screencap of [Redweb](http://i.imgur.com/qxwhC.png).

Nota bene
-----------

I haven't worked on or actively maintained this project in over a year. However I am now merging in pull requests, 
so I will make a best effort to keep this repo maintained.


Install and Run
---------------

Installation is simple. The only requirements are a running [Redis](http://code.google.com/p/redis/ "Redis") server, 
[Bottle](http://github.com/defnull/bottle "Bottle"), and the Python interface for Redis [redis-py](http://github.com/andymccurdy/redis-py "redis-py").

Install Bottle and redis-py:

    pip install bottle
    pip install redis

Start your Redis server, head to the Redweb directory, and then:

`python redweb.py`

The web interface will start on localhost, so point your browser to `http://127.0.0.1:8080/`. 


What You Can Do
---------------

Through a web interface, you will be able to add access the Redis INFO command, search for (and delete) keys, and use most 
of the Redis commands that existed the last time this was actively maintained (April 2010). 

More
------

Thanks to Antonio Ognio for Redis hash implementation, and Mark Erdmann for various additions, including AJAX support.


MIT License
------------
Copyright (c) 2010-2012 Ted Nyman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.



