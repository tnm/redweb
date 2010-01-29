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

@route('/delete/', method='POST')
@view('central')
def template_delete():

    key_delete = request.POST.get('key_delete', '').strip()
    r.delete(key_delete)
    db_size = r.dbsize()	
	   
    return dict(db_size = db_size, key=key_delete)

@route('/delete/all/', method='POST')
@view('central')
def template_delete_all():

   delete_all = request.POST.get('delete_all', '').strip()
   r.flushdb()
   db_size = r.dbsize()

   return dict(db_size = db_size)

# String functionality 

@route('/strings/add/', method='POST')
@view('strings')
def template_add():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()

    r.set(key,value)
    db_size = r.dbsize()
 
    return dict(key=key, db_size=db_size, value=value)

@route('/strings/show/:key')
@view('strings')
def template_show(key):
    key = key
    value = r.get(key)	
	
    return dict(key=key, value=value)	

# List Functionality

@route('/lists/push/', method='POST')
@view('lists')
def template_lists_push():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()

    r.push(key,member)
    db_size = r.dbsize()
 
    return dict(key=key, db_size=db_size, value=value)

@route('/lists/length/:key')
@view('lists')
def template_lists_length():
    key = key
    length = r.llen(key)
    dbsize = r.dbsize()

    return dict(key=key, length=length, db_size=db_size)

@route('/lists/range/' method='POST')
@view('lists')
def template_lists_range():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()

    range = r.lrange(key, start, end)
    db_size = r.dbsize()

    return dict(key=key,range=range,db_size=db_size)


@route('/lists/pop/' method='POST')
@view('lists')
def template_lists_pop):
    key = request.POST.get('key', '').strip()
    pop = r.pop(key)
    dbsize = r.dbsize()

    return dict(key=key, db_size=db_size)

# Set Functionality

@route('/sets/add/', method='POST')
@view('sets')
def template_sets_add():
   key = request.post.get('key', '').strip()
   member = request.post.get('member', '').strip()

   set_add = r.sadd(key, member)
   db_size = r.dbsize()  
 
   return dict(key=key, value=value, db_size=db_size)      

@route('/sets/remove/', method='POST')
@view('sets')
def template_sets_remove():
   key = request.post.get('key', '').strip()
   member = request.post.get('member', '').strip()

   set_remove = r.srem(key, member)
   db_size = r.dbsize()  
  
   return dict(key=key, value=value, db_size=db_size)      

@route('/sets/cardinality/:key')
@view('sets')
def template_lists_length():
    key = key 
    cardinality = r.scard(key)
    dbsize = r.dbsize()

    return dict(key=key, cardinality=cardinality, db_size=db_size)

"""
SMEMBERS | return all members of a set
"""

@route('/sets/members/', method='POST')
@view('sets')
def template_lists_smembers():
    key = key
    members = r.smembers(key)
    dbsize = r.dbsize()
  
    return dict(key=key, members=members, db_size=db_size)

"""
SRANDMEMBER | return a random member of set, without removing it
"""

@route('/sets/random/', method='POST')
@view('sets')
def template_lists_srandom():
    key = key
    random_member = r.srandmember(key)
    dbsize = r.dbsize()
  
    return dict(key=key, random_member=random_member, db_size=db_size)

# Sorted Set Functionality

@route('/zsets/add/', method='POST')
@view('zsets')
def template_zsets_add():
   key = request.post.get('key', '').strip()
   member = request.post.get('member', '').strip()

   zset_add = r.zadd(key, member)
   db_size = r.dbsize()  
 
   return dict(key=key, value=value, db_size=db_size)      

@route('/zsets/remove/', method='POST')
@view('zsets')
def template_zsets_remove():
   key = request.post.get('key', '').strip()
   member = request.post.get('member', '').strip()

   zset_remove = r.zrem(key, member)
   db_size = r.dbsize()  
  
   return dict(key=key, value=value, db_size=db_size)      

run()
