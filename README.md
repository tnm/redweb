##RedBottle

RedBottle is a small, pluggable application skeleton that's designed to neatly integrate Bottle
with Redis. Bottle is a simple, yet powerful Python framework, with built-in routing and templating. Redis
is a fast, powerful, persistent key-value store. Combined, they make a dynamite combination!

RedBottle uses a straight-forward, REST-like style to add, remove, and show key-values.

Install and Configure
---------------------

You'll need [Bottle](http://github.com/defnull/bottle "Bottle"), [Redis](http://code.google.com/p/redis/ "Redis"), and the [Python interface](http://github.com/andymccurdy/redis-py/ "Python Interface") for Redis.

If you have those installed, start your Redis server. Then:

`python redbottle.py` 

and the RedBottle application will start on localhost. Now you can build your application around it.

It's important to note that there is no built-in data sanitization, beyond what is built
in to Bottle. So if you need to do some particular sanitization, please roll your own.


Do Stuff
---------

Let's say you want to add a key-value the number '2' as a key and the name 'John' as its value.
It's as easy as utilizing POST at:

**/keyvalue/**

That saves it to the Redis data store.

To show the value of any key:

**/keyvalue/show/[key]**

Additions
----------
Modular additions, such as error messages and client-side validation, are on the to-do list. For the initial version,
the idea is to keep RedBottle as simple as possible, so developers can customize it as they see fit.

Author
------

Ted Nyman - @tnm8

A [blog post](http://philosophyofweb.com/2010/01/bottle-py-redis-redbottle/ "Post") about RedBottle


MIT License
-----------

 Copyright (c) 2010 Ted Nyman

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.

