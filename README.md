RedBottle is a small, pluggable application skeleton that designed to neatly integrate Bottle
with Redis. Bottle is a simple Python framework, with built-in routing and templating. Redis
is a sophisticated, persistent key-value store. They make a dynamite combination!

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

