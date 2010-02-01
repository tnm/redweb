__author__ = 'Ted Nyman'
__version__ = '0.1.0'
__license__ = 'MIT'

from bottle import route, request, response, view, send_file, run
import redis
import bottle

# Bottle debug - remove in production!
bottle.debug(True)

# The main redis object
r = redis.Redis()

# returned_value defaults to empty string
returned_value = ""

# Set static file routing
@route('/static/:filename')
def static_file(filename):
    send_file(filename, root='../redweb/static')



# Home route
@route('/')
@view('central')
def template_keyvalue():
   db_size = r.dbsize()
   all_keys = r.keys('*')
  
   return dict(returned_value=returned_value, all_keys=all_keys, db_size=db_size)

"""
Actions for all data types
"""
 
@route('/delete/', method='POST')
@view('central')
def template_delete():

    key_delete = request.POST.get('key_delete', '').strip()
    r.delete(key_delete)
    db_size = r.dbsize()
    all_keys = r.keys('*')
	   
    return dict(db_size = db_size, all_keys = all_keys, returned_value=returned_value, key=key_delete)

@route('/delete/all/', method='POST')
@view('central')
def template_delete_all():

    delete_all = request.POST.get('delete_all', '').strip()
    r.flushdb()
    all_keys = r.keys('*')

    db_size = r.dbsize()

    return dict(all_keys=all_keys, db_size = db_size)


"""
Strings
""" 

# SET | set a string value for a given key
@route('/strings/set/', method='POST')
@view('central')
def template_strings_set():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()
    r.set(key,value)
    all_keys = r.keys('*')
    db_size = r.dbsize()
 
    return dict(key=key, value=value, returned_value=returned_value, all_keys=all_keys, db_size=db_size)


# GET | return the string value of a key
@route('/strings/get/', method='POST')
@view('central')
def template_string_get():
    key = request.POST.get('key', '').strip()
    returned_value = r.get(key)	
    all_keys = r.keys('*')
    db_size = r.dbsize()
	
    return dict(key=key, returned_value=returned_value, all_keys=all_keys, db_size=db_size)	


"""
Lists

"""

# RPUSH | append an element to the tail of a list
@route('/lists/rightpush/', method='POST')
@view('central')
def template_lists_rightpush():
    key = request.POST.get('key', '').strip()
    element = request.POST.get('element', '').strip()
    r.push(key,element)
    all_keys = r.keys('*')
    db_size = r.dbsize()
 
    return dict(key=key, element=element, returned_value=returned_value, all_keys=all_keys, db_size=db_size)


# LPUSH | append an element to the head of a list
@route('/lists/leftpush/', method='POST')
@view('central')
def template_lists_leftpush():
    key = request.POST.get('key', '').strip()
    element = request.POST.get('element', '').strip()
    r.push(key,element, tail=True)
    all_keys = r.keys('*')
    db_size = r.dbsize()
 
    return dict(key=key, element=element, returned_value=returned_value, all_keys=all_keys, db_size=db_size)


# LLEN | return the length of a list
@route('/lists/length/', method='POST')
@view('central')
def template_lists_length():
    key = request.POST.get('key', '').strip()
    llen = r.llen(key)
    all_keys = r.keys('*')
    dbsize = r.dbsize()

    return dict(key=key, returned_value=llen, all_keys=all_keys, db_size=db_size)


# LRANGE | return a range of elements from a list
@route('/lists/range/', method='POST')
@view('central')
def template_lists_range():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    list_range = r.lrange(key, start, end)
    all_keys = r.keys('*')
    db_size = r.dbsize()

    return dict(key=key, list_range=list_range, returned_value=returned_value, all_keys=all_keys, db_size=db_size)

# LTRIM
# LINDEX
# LSET
# LREM


# LPOP | return and remove the first element of a list
@route('/lists/pop/', method='POST')
@view('central')
def template_lists_lpop():
    key = request.POST.get('key', '').strip()
    left_pop = r.pop(key)
    all_keys = r.keys('*')
    dbsize = r.dbsize()

    return dict(key=key, returned_value=left_pop, all_keys=all_keys, db_size=db_size)


# RPOP | return and remove the last element of a list
@route('/lists/pop/', method='POST')
@view('central')
def template_lists_rpop():
    key = request.POST.get('key', '').strip()
    right_pop = r.pop(key, tail=True)
    all_keys = r.keys('*')
    dbsize = r.dbsize()

    return dict(key=key, returned_value=right_pop, all_keys=all_keys, db_size=db_size)

# BLPOP
# BRPOP
# RPOPLPPUSH


"""
Sets
"""

# SADD | add a member to a set
@route('/sets/add/', method='POST')
@view('central')
def template_sets_add():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    set_add = r.sadd(key, member)
    all_keys = r.keys('*')
    db_size = r.dbsize()  
 
    return dict(key=key, member=member, returned_value=returned_value, all_keys=all_keys, db_size=db_size)      


# SREM | remove a member of a set
@route('/sets/remove/', method='POST')
@view('central')
def template_sets_remove():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    set_remove = r.srem(key, member)
    all_keys = r.keys('*')
    db_size = r.dbsize()  
  
    return dict(key=key, member=member, returned_value=returned_value, all_keys=all_keys, db_size=db_size)      


# SPOP
# SMOVE

# SCARD | return the cardinality for a set
@route('/sets/cardinality/', method='POST')
@view('central')
def template_sets_cardinality():
    key = request.POST.get('key', '').strip() 
    cardinality = r.scard(key)
    all_keys = r.keys('*')
    dbsize = r.dbsize()

    return dict(key=key, returned_value=cardinality, all_keys=all_keys, db_size=db_size)

# SISMEMBER
# SINTER | for any number of sets, return the values that those sets all share
# SINTERSTORE
# SUNION
# SUNIONSTORE
# SDIFF
# SDIFFSTORE

# SMEMBERS | return all members of a set
@route('/sets/members/', method='POST')
@view('central')
def template_sets_members():
    key = key
    members = r.smembers(key)
    all_keys = r.keys('*')
    dbsize = r.dbsize()
  
    return dict(key=key, returned_value=members, all_keys=all_keys, db_size=db_size)


# SRANDMEMBER | return a random member of set, without removing it
@route('/sets/random/', method='POST')
@view('central')
def template_sets_srandom():
    key = key
    random_member = r.srandmember(key)
    all_keys = r.keys('*')
    dbsize = r.dbsize()
  
    return dict(key=key, returned_value=random_member, all_keys=all_keys, db_size=db_size)


"""
Sorted Sets
"""

# ZADD | add a member to a sorted set
@route('/zsets/add/', method='POST')
@view('central')
def template_zsets_add():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    zset_add = r.zadd(key, member)
    all_keys = r.keys('*')
    db_size = r.dbsize()  
 
    return dict(key=key, value=value, returned_value=returned_value, all_keys=all_keys, db_size=db_size)      


# ZREM | remove a member of a sorted set
@route('/zsets/remove/', method='POST')
@view('central')
def template_zsets_remove():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    zset_remove = r.zrem(key, member)
    all_keys = r.keys('*')
    db_size = r.dbsize()  
  
    return dict(key=key, member=member, returned_value=returned_value, all_keys=all_keys, db_size=db_size)      

# ZINCRBY
# ZCRANGE
# ZREVRANGE
# ZRANGEBYSCORE

# ZCARD | return the cardinality for a set
@route('/zsets/cardinality/', method='POST')
@view('central')
def template_zsets_cardinality():
    key = request.POST.get('key', '').strip() 
    cardinality = r.zcard(key)
    all_keys = r.keys('*')
    dbsize = r.dbsize()

    return dict(key=key, returned_value=cardinality, all_keys=all_keys, db_size=db_size)

# ZSCORE
# ZREMRANGEBYSCORE


"""
Sorting, Persistence, Remote Server
"""

# SORT

# BGSAVE
# LASTSAVE
# SHUTDOWN
# BGREWRITEAOF

# INFO
# MONITOR
# SLAVE

#run it!
run()
