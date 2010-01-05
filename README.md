RedBottle is a small, pluggable application skeleton that's designed to neatly integrate Bottle
with Redis. Bottle is a simple, yet powerful Python framework, with built-in routing and templating. Redis
is a fast, powerful, persistent key-value store. Combined, they make a dynamite combination!

RedBottle uses a straight-forward, RESTful style to add, remove, and show key-values.

Install and Configure
---------------------

You'll need Bottle, Redis, and the Python wrapper for Redis.

If you have those installed, start your Redis server. Then:

python redbottle.py

and the application will start on localhost. Now build your application around it.

It's important to note that there is no built-in data sanitization, beyond what is built
in to Bottle. So if you need to do some particular sanitization, please roll your own.


Do Stuff
---------

Let's say you want to add a key-value with the number 2 as a key and the name 'John' as its value.
It's as easy as utilizing the REST resource at:

/keyvalue/2/John/add

That saves it to the Redis data store.

To delete it:

/keyvalue/2/John/delete

To view the value associated with the key:

/keyvalue/2/


Author
------

Ted Nyman : @tnm8

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

