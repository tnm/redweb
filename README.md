Redweb
-------

Redweb is a web interface to the Redis key-value store. It is written in Python, powered by the Bottle micro-framework. You can think of redweb as something like phpMyAdmin, but for Redis (and written in Python, of course).

But Redweb is more than that, too. The source can be reused to create web applications that utilize Bottle and Redis. For example, you should be able to piece together code from Redweb and (with some additions) cook up a simple Twitter clone. So Redweb is sort of like a reversable jacket -- two neat things for the price of one. Well, no price actually, as Redweb is MIT-licensed and wants to be forked.

The basic idea derives from my super-simple RedBottle project.

Install and Run
---------------

Installation is simple. The only requirements are Redis, Bottle, and the Python interface for the Redis (the latter two are included here). For now, I recommend using the version of redis-py included here (http://github.com/razmataz/redis-py), for its proper string handling (the main trunk of redis-py will soon have similar changes).

With Bottle and Python in your PYTHONPATH, start your Redis server, and then:

python redweb.py

and the interface will start on localhost. 

More and To Do
---------------

Redweb is certainly alpha. It implements most of core Redis functionality, but there is still more to be added. My plan is to include ALL Redis functionality.

I will also keep Redweb up-to-date with updates to Redis, which is constantly being improved.

Author: Ted Nyman - @tnm8

MIT License
------------
Copyright (c) 2010 Ted Nyman
