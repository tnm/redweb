redweb
=======

**redweb** is a super simple web display of information about a set of
Redis servers. It just provides the content of the `INFO` command in a
nice format, for any number of Redis instances.

requirements
--------------

* sinatra `gem install sinatra`
* redis-rb `gem install redis`

to run
----------------

```
ruby redweb.rb [path/to/your_config_file.yml]
```

config file
--------------

The config file is a YAML file, and it's where you tell **redweb**
the hostname and port for your Redis servers. It must be structured
like this:

```
redis1:
  hostname: 127.0.0.1
  port: 6390

redis2:
  hostname: 127.0.0.1
  port: 6391

redis3:
  hostname: 127.0.0.1
  port: 6392
```

**redweb** will use the names (like `redis1`) as identifiers.

license
---------
MIT
