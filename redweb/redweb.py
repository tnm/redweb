__author__ = 'Ted Nyman'
__version__ = '0.1.2'
__license__ = 'MIT'

from bottle import route, request, response, view, send_file, run
import redis
import bottle

# Bottle debug - remove in production!

bottle.debug(True)

# The main redis object

r = redis.Redis()

# Set static file routing

@route('/static/:filename')
def static_file(filename):
    send_file(filename, root='../redbottle/static')

# Central page for all operations

@route('/central/')
@view('central')
def template_keyvalue():  
    db_size = r.dbsize()
    return dict(db_size=db_size)

# Universal functionality

@route('/delete/', method='post')
@view('central')
def template_delete():

    key_delete = request.post.get('key_delete', '').strip()
    r.delete(key_delete)
    db_size = r.dbsize()	
	   
    return dict(db_size = db_size, key=key_delete)

@route('/delete/all/', method='post')
@view('central')
def template_delete_all():

   delete_all = request.post.get('delete_all', '').strip()
   r.flushdb()
   db_size = r.dbsize()

   return dict(db_size = db_size)

# String functionality 

@route('/strings/add/', method='post')
@view('strings')
def template_add():
    key = request.post.get('key', '').strip()
    value = request.post.get('value', '').strip()

    r.set(key,value)
    db_size = r.dbsize()
 
    return dict(key=key, db_size=db_size, value=value)

@route('/strings/show/' method='post')
@view('strings')
def template_show(key):
    key = request.post.get('key', '').strip()
    show_value = r.get(key)	
	
    return dict(key=key, show_value=show_value)	

# List Functionality

@route('/lists/push/', method='post')
@view('lists')
def template_lists_push():
    key = request.post.get('key', '').strip()
    member = request.post.get('member', '').strip()

    r.push(key,member)
    db_size = r.dbsize()
 
    return dict(key=key, member=member, db_size=db_size)

"""
LLEN | return the length of a list
"""

@route('/lists/length/' method='post':)
@view('lists')
def template_lists_length():
    key = request.post.get('key', '').strip()
    length = r.llen(key)
    dbsize = r.dbsize()

    return dict(key=key, length=length, db_size=db_size)

@route('/lists/range/' method='post')
@view('lists')
def template_lists_range():
    key = request.post.get('key', '').strip()
    start = request.post.get('start', '').strip()
    end = request.post.get('end', '').strip()

    range = r.lrange(key, start, end)
    db_size = r.dbsize()

    return dict(key=key, range=range, db_size=db_size)

@route('/lists/pop/' method='post')
@view('lists')
def template_lists_pop):
    key = request.post.get('key', '').strip()
    pop = r.pop(key)
    dbsize = r.dbsize()

    return dict(key=key, db_size=db_size)

# Set Functionality

"""
SADD | add a member to a set
"""

@route('/sets/add/', method='post')
@view('sets')
def template_sets_add():
   key = request.post.get('key', '').strip()
   member = request.post.get('member', '').strip()

   set_add = r.sadd(key, member)
   db_size = r.dbsize()  
 
   return dict(key=key, value=value, db_size=db_size)      

"""
SREM | remove a member of a set
"""

@route('/sets/remove/', method='post')
@view('sets')
def template_sets_remove():
   key = request.post.get('key', '').strip()
   member = request.post.get('member', '').strip()

   set_remove = r.srem(key, member)
   db_size = r.dbsize()  
  
   return dict(key=key, value=value, db_size=db_size)      

"""
SCARD | return the cardinality for a set
"""

@route('/sets/cardinality/' method='post')
@view('sets')
def template_lists_length():
    key = request.post.get('key', '').strip() 
    cardinality = r.scard(key)
    dbsize = r.dbsize()

    return dict(key=key, cardinality=cardinality, db_size=db_size)

"""
SMEMBERS | return all members of a set
"""

@route('/sets/members/', method='post')
@view('sets')
def template_lists_smembers():
    key = key
    members = r.smembers(key)
    dbsize = r.dbsize()
  
    return dict(key=key, members=members, db_size=db_size)

"""
SRANDMEMBER | return a random member of set, without removing it
"""

@route('/sets/random/', method='post')
@view('sets')
def template_lists_srandom():
    key = key
    random_member = r.srandmember(key)
    dbsize = r.dbsize()
  
    return dict(key=key, random_member=random_member, db_size=db_size)

# Sorted Set Functionality

"""
ZADD | add a member to a sorted set
"""

@route('/zsets/add/', method='post')
@view('zsets')
def template_zsets_add():
   key = request.post.get('key', '').strip()
   member = request.post.get('member', '').strip()

   zset_add = r.zadd(key, member)
   db_size = r.dbsize()  
 
   return dict(key=key, value=value, db_size=db_size)      

"""
ZREM | remove a member of a sorted set
"""

@route('/zsets/remove/', method='post')
@view('zsets')
def template_zsets_remove():
   key = request.post.get('key', '').strip()
   member = request.post.get('member', '').strip()

   zset_remove = r.zrem(key, member)
   db_size = r.dbsize()  
  
   return dict(key=key, member=member, db_size=db_size)      

#run it!
run()
