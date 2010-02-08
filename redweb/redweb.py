"""
Redweb is a web interface to the Redis key-value store and server. It is written in Python, and is built on the
Bottle micro-framework. With Redweb, you can easily interact with the Redis database through your
web browser, utilizing POST functionality.
	
	8 Feb 2010 | all functions return either a status code, value, or other (0.1.1)
	5 Feb 2010 | additional set functionality, UI improvements
	2 Feb 2010 | first public release (0.1.0)
"""

__author__ = 'Ted Nyman'
__version__ = '0.1.1'
__license__ = 'MIT'


from bottle import route, request, response, view, send_file, run
import redis
import bottle
import string

# Bottle debug - remove in production!
bottle.debug(True)

# The main redis object
r = redis.Redis()

# returned_value defaults to empty string
returned_value = ""

# search_result defaults to empty string
search_result = ""

# Set static file routing
@route('/static/:filename')
def static_file(filename):
    send_file(filename, root='../redweb/static')

# Home route
@route('/')
@view('central')
def template_keyvalue():
   db_size = r.dbsize()
  
   return dict(returned_value=returned_value, db_size=db_size, search_result=search_result)

"""
Actions for all data types
"""
 
@route('/delete/', method='POST')
@view('central')
def template_delete():

    key_delete = request.POST.get('key_delete', '').strip()
    r.delete(key_delete)
    db_size = r.dbsize()
	   
    return dict(db_size = db_size, returned_value=returned_value, search_result=search_result, key=key_delete)

@route('/delete/all/', method='POST')
@view('central')
def template_delete_all():

    delete_all = request.POST.get('delete_all', '').strip()
    r.flushdb()
    db_size = r.dbsize()

    return dict(db_size=db_size, search_result=search_result)

@route('/search/', method='POST')
@view('central')
def template_search():
    key = request.POST.get('key', '').strip()
    search_result = r.keys(key)
    db_size = r.dbsize()

    return dict(db_size=db_size, returned_value=returned_value, search_result=search_result)


"""
Strings
""" 

# SET | set a string value for a given key
@route('/strings/set/', method='POST')
@view('central')
def template_strings_set():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()
    set = r.set(key,value)
    db_size = r.dbsize()
 
    return dict(key=key, value=value, returned_value=set, db_size=db_size, search_result=search_result)


# GET | return the string value of a key
@route('/strings/get/', method='POST')
@view('central')
def template_string_get():
    key = request.POST.get('key', '').strip()
    get = r.get(key)	
    db_size = r.dbsize()
	
    return dict(key=key, returned_value=get,  db_size=db_size, search_result=search_result)	


"""
Lists

"""

# RPUSH | append an element to the tail of a list
@route('/lists/rightpush/', method='POST')
@view('central')
def template_lists_rightpush():
    key = request.POST.get('key', '').strip()
    element = request.POST.get('element', '').strip()
    right_push = r.push(key,element)
    db_size = r.dbsize()
 
    return dict(key=key, element=element, returned_value=right_push, db_size=db_size, search_result=search_result)


# LPUSH | append an element to the head of a list
@route('/lists/leftpush/', method='POST')
@view('central')
def template_lists_leftpush():
    key = request.POST.get('key', '').strip()
    element = request.POST.get('element', '').strip()
    left_push = r.push(key,element, tail=True)
    db_size = r.dbsize()
 
    return dict(key=key, element=element, returned_value=left_push, db_size=db_size, search_result=search_result)


# LLEN | return the length of a list
@route('/lists/length/', method='POST')
@view('central')
def template_lists_length():
    key = request.POST.get('key', '').strip()
    llen = r.llen(key)
    db_size = r.dbsize()

    return dict(key=key, returned_value=llen, db_size=db_size, search_result=search_result)


# LRANGE | return a range of elements from a list
@route('/lists/range/', method='POST')
@view('central')
def template_lists_range():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    list_range = r.lrange(key, start, end)
    db_size = r.dbsize()

    return dict(key=key, returned_value=list_range, db_size=db_size, search_result=search_result)

# LTRIM
# LINDEX
# LSET
# LREM


# LPOP | return and remove the first element of a list
@route('/lists/leftpop/', method='POST')
@view('central')
def template_lists_lpop():
    key = request.POST.get('key', '').strip()
    left_pop = r.pop(key)
    db_size = r.dbsize()

    return dict(key=key, returned_value=left_pop, db_size=db_size, search_result=search_result)


# RPOP | return and remove the last element of a list
@route('/lists/rightpop/', method='POST')
@view('central')
def template_lists_rpop():
    key = request.POST.get('key', '').strip()
    right_pop = r.pop(key, tail=True)
    db_size = r.dbsize()

    return dict(key=key, returned_value=right_pop, db_size=db_size, search_result=search_result)

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
    db_size = r.dbsize()  
 
    return dict(key=key, member=member, returned_value=set_add, db_size=db_size, search_result=search_result)      


# SREM | remove a member of a set
@route('/sets/remove/', method='POST')
@view('central')
def template_sets_remove():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    set_remove = r.srem(key, member)
    db_size = r.dbsize()  
  
    return dict(key=key, member=member, returned_value=set_remove, db_size=db_size, search_result=search_result)      


# SPOP | return and remove a random member from a set
@route('/sets/pop/', method='POST')
@view('central')
def template_sets_pop():
    key = request.POST.get('key', '').strip()
    random_pop = r.spop(key)
    db_size = r.dbsize()  
  
    return dict(key=key, member=member, returned_value=random_pop, db_size=db_size, search_result=search_result)      

# SMOVE | move a member of a one set to another set
@route('/sets/move/', method='POST')
@view('central')
def template_sets_move():
    source_key = request.POST.get('source_key', '').strip()
    destination_key = request.POST.get('destination_key', '').strip()
    member = request.POST.get('member', '').strip()
    smove = r.smove(source_key, destination_key, member)
    db_size = r.dbsize()
 
    return dict(member=member, returned_value=smove, db_size=db_size, search_result=search_result)      


# SCARD | return the cardinality for a set
@route('/sets/cardinality/', method='POST')
@view('central')
def template_sets_cardinality():
    key = request.POST.get('key', '').strip() 
    cardinality = r.scard(key)
    db_size = r.dbsize()

    return dict(key=key, returned_value=cardinality, db_size=db_size, search_result=search_result)


# SISMEMBER | check if a member is stored at a key - returns 1 if true, 0 if false
@route('/sets/ismember/', method='POST')
@view('central')
def template_sets_ismember():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    is_member = r.sismember(key, member)
    db_size = r.dbsize()  
 
    return dict(key=key, member=member, returned_value=is_member, db_size=db_size, search_result=search_result)      

# SINTER | for any number of sets, return the intersection
@route('/sets/intersection/', method='POST')
@view('central')
def template_sets_intersection():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    intersection = r.sinter('%s' % ' '.join(tuple_keys))
    db_size = r.dbsize()
  
    return dict(key=key, returned_value=intersection, db_size=db_size, search_result=search_result)


# SINTERSTORE | for any number of sets, return the intersection and store it as a new key
@route('/sets/interstore/', method='POST')
@view('central')
def template_sets_interstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    interstore = r.sinterstore('%s %s' % (destination_key, ' '.join(tuple_keys)))
    db_size = r.dbsize()
  
    return dict(key=key, returned_value=interstore, db_size=db_size, search_result=search_result)


# SUNION | for any number of sets, return the union
@route('/sets/union/', method='POST')
@view('central')
def template_sets_union():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    union = r.sunion('%s' % ' '.join(tuple_keys))
    db_size = r.dbsize()
  
    return dict(key=key, returned_value=union, db_size=db_size, search_result=search_result)


# SUNIONSTORE | for any number of sets, return the union and store it as a new key
@route('/sets/unionstore/', method='POST')
@view('central')
def template_sets_unionstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    unionstore = r.sunionstore('%s %s' % (destination_key, ' '.join(tuple_keys)))
    db_size = r.dbsize()
  
    return dict(key=key, returned_value=unionstore, db_size=db_size, search_result=search_result)


# SDIFF | for any number of sets, return the difference
@route('/sets/difference/', method='POST')
@view('central')
def template_sets_difference():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    difference = r.sunion('%s' % ' '.join(tuple_keys))
    db_size = r.dbsize()
  
    return dict(key=key, returned_value=difference, db_size=db_size, search_result=search_result)


# SDIFFSTORE | for any number of sets, return the difference and store it as a new key

@route('/sets/diffstore/', method='POST')
@view('central')
def template_sets_diffstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    diffstore = r.sdiffstore('%s %s' % (destination_key, ' '.join(tuple_keys)))
    db_size = r.dbsize()
  
    return dict(key=key, returned_value=diffstore, db_size=db_size, search_result=search_result)


# SMEMBERS | return all members of a set
@route('/sets/members/', method='POST')
@view('central')
def template_sets_members():
    key = request.POST.get('key', '').strip()
    members = r.smembers(key)
    db_size = r.dbsize()
  
    return dict(key=key, returned_value=members, db_size=db_size, search_result=search_result)


# SRANDMEMBER | return a random member of set, without removing it
@route('/sets/random/', method='POST')
@view('central')
def template_sets_srandom():
    key = request.POST.get('key', '').strip()
    random_member = r.srandmember(key)
    db_size = r.dbsize()
  
    return dict(key=key, returned_value=random_member, db_size=db_size, search_result=search_result)


"""
Sorted Sets
"""

# ZADD | add a member to a sorted set
@route('/zsets/add/', method='POST')
@view('central')
def template_zsets_add():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    score = request.POST.get('score', '').strip()
    zset_add = r.zadd(key, member, score)
    db_size = r.dbsize()  
 
    return dict(key=key, member=member, score=score, returned_value=zset_add, db_size=db_size, search_result=search_result)      


# ZREM | remove a member of a sorted set
@route('/zsets/remove/', method='POST')
@view('central')
def template_zsets_remove():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    zset_remove = r.zrem(key, member)
    db_size = r.dbsize()  
  
    return dict(key=key, member=member, returned_value=zset_remove, db_size=db_size, search_result=search_result)      

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
    db_size = r.dbsize()

    return dict(key=key, returned_value=cardinality, db_size=db_size, search_result=search_result)

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
