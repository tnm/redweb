__author__ = 'Ted Nyman'
__version__ = '0.1.0'
__license__ = 'MIT'

from bottle import route, request, response, view, send_file, run
import redis
import bottle

# PRELIMINARIES

# Bottle debug - remove in production!
bottle.debug(True)

# The main redis object
r = redis.Redis()

# Set static file routing
@route('/static/:filename')
def static_file(filename):
    send_file(filename, root='../redbottle/static')

# CENTRAL

# Central page for all operations
@route('/central/')
@view('central')
def template_keyvalue():  
    db_size = r.dbsize()
    return dict(db_size=db_size)

# UNIVERSALS 

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


# STRINGS 

# SET | set a string value for a given key
@route('/strings/set/', method='post')
@view('central')
def template_set():
    key = request.post.get('key', '').strip()
    value = request.post.get('value', '').strip()

    r.set(key,value)
    db_size = r.dbsize()
 
    return dict(key=key, db_size=db_size, value=value)


# GET | return the string value of a key
@route('/strings/get/' method='post')
@view('central')
def template_get(key):
    key = request.post.get('key', '').strip()
    show_value = r.get(key)	
	
    return dict(key=key, show_value=show_value)	


# LISTS

# RPUSH | append an element to the tail of a list
@route('/lists/rightpush/', method='post')
@view('central')
def template_lists_rightpush():
    key = request.post.get('key', '').strip()
    element = request.post.get('element', '').strip()

    r.push(key,member)
    db_size = r.dbsize()
 
    return dict(key=key, element=element, db_size=db_size)


# LPUSH | append an element to the head of a list
@route('/lists/leftpush/', method='post')
@view('central')
def template_lists_leftpush():
    key = request.post.get('key', '').strip()
    element = request.post.get('element', '').strip()

    r.push(key,element, tail=True)
    db_size = r.dbsize()
 
    return dict(key=key, element=element, db_size=db_size)


# LLEN | return the length of a list
@route('/lists/length/' method='post':)
@view('central')
def template_lists_length():
    key = request.post.get('key', '').strip()
    length = r.llen(key)
    dbsize = r.dbsize()

    return dict(key=key, length=length, db_size=db_size)


# LRANGE | return a range of elements from a list
@route('/lists/range/' method='post')
@view('central')
def template_lists_range():
    key = request.post.get('key', '').strip()
    start = request.post.get('start', '').strip()
    end = request.post.get('end', '').strip()
    list_range = r.lrange(key, start, end)
    db_size = r.dbsize()

    return dict(key=key, list_range=list_range, db_size=db_size)

# LTRIM
# LINDEX
# LSET
# LREM


# LPOP | return and remove the first element of a list
@route('/lists/pop/' method='post')
@view('central')
def template_lists_lpop):
    key = request.post.get('key', '').strip()
    pop = r.pop(key)
    dbsize = r.dbsize()

    return dict(key=key, db_size=db_size)


# RPOP | return and remove the last element of a list
@route('/lists/pop/' method='post')
@view('central')
def template_lists_rpop):
    key = request.post.get('key', '').strip()
    pop = r.pop(key, tail=True)
    dbsize = r.dbsize()

    return dict(key=key, db_size=db_size)

# BLPOP
# BRPOP
# RPOPLPPUSH


# SETS

# SADD | add a member to a set
@route('/sets/add/', method='post')
@view('central')
def template_sets_add():
    key = request.post.get('key', '').strip()
    member = request.post.get('member', '').strip()
    set_add = r.sadd(key, member)
    db_size = r.dbsize()  
 
    return dict(key=key, value=value, db_size=db_size)      


# SREM | remove a member of a set
@route('/sets/remove/', method='post')
@view('central')
def template_sets_remove():
    key = request.post.get('key', '').strip()
    member = request.post.get('member', '').strip()
    set_remove = r.srem(key, member)
    db_size = r.dbsize()  
  
    return dict(key=key, value=value, db_size=db_size)      


# SPOP
# SMOVE

# SCARD | return the cardinality for a set
@route('/sets/cardinality/' method='post')
@view('central')
def template_sets_cardinality():
    key = request.post.get('key', '').strip() 
    cardinality = r.scard(key)
    dbsize = r.dbsize()

    return dict(key=key, cardinality=cardinality, db_size=db_size)

# SISMEMBER
# SINTER | for any number of sets, return the values that those sets all share
# SINTERSTORE
# SUNION
# SUNIONSTORE
# SDIFF
# SDIFFSTORE

# SMEMBERS | return all members of a set
@route('/sets/members/', method='post')
@view('central')
def template_sets_members():
    key = key
    members = r.smembers(key)
    dbsize = r.dbsize()
  
    return dict(key=key, members=members, db_size=db_size)


# SRANDMEMBER | return a random member of set, without removing it
@route('/sets/random/', method='post')
@view('central')
def template_sets_srandom():
    key = key
    random_member = r.srandmember(key)
    dbsize = r.dbsize()
  
    return dict(key=key, random_member=random_member, db_size=db_size)


# SORTED SETS (ZSETS)

# ZADD | add a member to a sorted set
@route('/zsets/add/', method='post')
@view('central')
def template_zsets_add():
    key = request.post.get('key', '').strip()
    member = request.post.get('member', '').strip()

    zset_add = r.zadd(key, member)
    db_size = r.dbsize()  
 
    return dict(key=key, value=value, db_size=db_size)      


# ZREM | remove a member of a sorted set
@route('/zsets/remove/', method='post')
@view('central')
def template_zsets_remove():
    key = request.post.get('key', '').strip()
    member = request.post.get('member', '').strip()

    zset_remove = r.zrem(key, member)
    db_size = r.dbsize()  
  
    return dict(key=key, member=member, db_size=db_size)      

# ZINCRBY
# ZCRANGE
# ZREVRANGE
# ZRANGEBYSCORE

# ZCARD | return the cardinality for a set
@route('/zsets/cardinality/' method='post')
@view('central')
def template_zsets_cardinality():
    key = request.post.get('key', '').strip() 
    cardinality = r.zcard(key)
    dbsize = r.dbsize()

    return dict(key=key, cardinality=cardinality, db_size=db_size)

# ZSCORE
# ZREMRANGEBYSCORE


# SORTING, PERSISTENCE, REMOTE SERVER

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
