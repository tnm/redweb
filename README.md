redweb
-------

redweb is a full web interface to the Redis key-value store. It is written in Python, powered by the Bottle micro-framework. You can think of redweb as something like a basic phpMyAdmin, but for Redis (and written in Python, of course).

But redweb is more than that, too. The code is easily reusable to create web applications that utilize Bottle and Redis. For example, it should be simple to piece together code from redweb (and, with some additions), cook up a simple Twitter clone.

The basic idea derives from my RedBottle project.

Install and Run
---------------

Installation is simple. The only requirements are Redis, Bottle, and the Python interface for the Redis (the latter two are included here). With Bottle and Python in your PYTHONPATH, start your Redis server, and then:

python redweb.py

and the interface will start on localhost. 

More and To Do
---------------

Author: Ted Nyman - @tnm8

I will do my best to keep redweb up-to-date with updates to Redis and redis-py. I'm also curious to see how people may use the redweb code in production -- please let me know!


MIT License
------------
Copyright (c) 2010 Ted Nyman
