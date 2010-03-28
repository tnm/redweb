"""
Redweb is a web interface to the Redis key-value store and server. It is written in Python, and is built on the
Bottle micro-framework. With Redweb, you can easily interact with the Redis database through your
web browser, utilizing POST functionality.

       15 Mar 2010 | Additional ZSET functionality
       13 Mar 2010 | Save and background save functionality added (0.2.1) 		
       28 Feb 2010 | Redweb requires refactored redis-py bindings (0.2.0)
	8 Feb 2010 | all current functions return either a status code, value, etc. (0.1.1)
	5 Feb 2010 | additional set functionality, UI improvements
	2 Feb 2010 | first public release (0.1.0)
"""

__author__ = 'Ted Nyman'
__version__ = '0.2.2'
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
   info = r.info()
 
   return dict(returned_value=returned_value, db_size=db_size, search_result=search_result, info=info)

### Actions for all data types ###
 
@route('/delete/', method='POST')
@view('central')
def template_delete():

    key_delete = request.POST.get('key_delete', '').strip()
    delete = r.delete(key_delete)
    db_size = r.dbsize()
    info = r.info()
	   
    return dict(returned_value=delete, db_size=db_size, search_result=search_result, info=info)


@route('/delete/all/', method='POST')
@view('central')
def template_delete_all():

    delete_all = request.POST.get('delete_all', '').strip()
    r.flushdb()
    db_size = r.dbsize()
    info = r.info()

    return dict(db_size=db_size, search_result=search_result, info=info)


@route('/search/', method='POST')
@view('central')
def template_search():
    key = request.POST.get('key', '').strip()
    search_result = r.keys(key)
    db_size = r.dbsize()
    info = r.info()

    return dict(returned_value=returned_value, db_size=db_size, search_result=search_result, info=info)


### Strings ###


# SET | set a string value for a given key
@route('/strings/set/', method='POST')
@view('central')
def template_strings_set():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()
    sset = r.set(key,value)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, value=value, returned_value=sset, db_size=db_size, search_result=search_result, info=info)


# GET | return the string value of a key
@route('/strings/get/', method='POST')
@view('central')
def template_string_get():
    key = request.POST.get('key', '').strip()
    get = r.get(key)	
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=get, db_size=db_size, search_result=search_result, info=info)	


# GETSET | set a string value for a key, only if the key does not exist, and return value
@route('/strings/getset/', method='POST')
@view('central')
def template_strings_getset():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()
    getset = r.getset(key,value)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, value=value, returned_value=getset, db_size=db_size, search_result=search_result, info=info)

# MGET

# SETNX | set a string value for a given key, only if the key does not exists
@route('/strings/setnx/', method='POST')
@view('central')
def template_strings_setnx():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()
    setnx = r.setnx(key,value)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, value=value, returned_value=setnx, db_size=db_size, search_result=search_result, info=info)


# MSET
# MSETNX

# INCR | increment a value by 1
@route('/strings/increment/', method='POST')
@view('central')
def template_string_increment():
    key = request.POST.get('key', '').strip()
    increment = r.incr(key)
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=increment, db_size=db_size, search_result=search_result, info=info)	


# INCRBY | increment a value by any amount
@route('/strings/incrementby/', method='POST')
@view('central')
def template_string_incrementby():
    key = request.POST.get('key', '').strip()
    amount = request.POST.get('amount', '').strip()
    incrementby = r.incr(key, amount)
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=incrementby, db_size=db_size, search_result=search_result, info=info)	

# DECR | decrement a value by 1
@route('/strings/decrement/', method='POST')
@view('central')
def template_string_decrement():
    key = request.POST.get('key', '').strip()
    decrement = r.decr(key)
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=decrement, db_size=db_size, search_result=search_result, info=info)	

# DECRBY | decrement a value by any amount
@route('/strings/decrementby/', method='POST')
@view('central')
def template_string_decrementby():
    key = request.POST.get('key', '').strip()
    amount = request.POST.get('amount', '').strip()
    decrementby = r.decr(key, amount)
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=decrementby, db_size=db_size, search_result=search_result, info=info)	


### Lists ###


# RPUSH | append an element to the tail of a list
@route('/lists/rightpush/', method='POST')
@view('central')
def template_lists_rightpush():
    key = request.POST.get('key', '').strip()
    element = request.POST.get('element', '').strip()
    right_push = r.rpush(key,element)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, element=element, returned_value=right_push, db_size=db_size, search_result=search_result, info=info)


# LPUSH | append an element to the head of a list
@route('/lists/leftpush/', method='POST')
@view('central')
def template_lists_leftpush():
    key = request.POST.get('key', '').strip()
    element = request.POST.get('element', '').strip()
    left_push = r.lpush(key,element)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, element=element, returned_value=left_push, db_size=db_size, search_result=search_result, info=info)


# LLEN | return the length of a list
@route('/lists/length/', method='POST')
@view('central')
def template_lists_length():
    key = request.POST.get('key', '').strip()
    llen = r.llen(key)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=llen, db_size=db_size, search_result=search_result, info=info)


# LRANGE | return a range of elements from a list
@route('/lists/range/', method='POST')
@view('central')
def template_lists_range():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    list_range = r.lrange(key, start, end)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=list_range, db_size=db_size, search_result=search_result, info=info)


# LTRIM | trim a list so that it contains just the specific range of elements
@route('/lists/trim/', method='POST')
@view('central')
def template_lists_range():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    ltrim = r.ltrim(key, start, end)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=ltrim, db_size=db_size, search_result=search_result, info=info)


# LINDEX | return the indexed element for a particular key
@route('/lists/lindex/', method='POST')
@view('central')
def template_lists_lindex():
    key = request.POST.get('key', '').strip()
    index = request.POST.get('index', '').strip()
    list_index = r.lindex(key, index)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, returned_value=list_index, db_size=db_size, search_result=search_result, info=info)


# LSET | set the list element at index
@route('/lists/set/', method='POST')
@view('central')
def template_lists_lset():
    key = request.POST.get('key', '').strip()
    index = request.POST.get('index', '').strip()
    element = request.POST.get('element', '').strip()
    lset = r.lset(key, index, element)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, returned_value=lset, db_size=db_size, search_result=search_result, info=info)


# LREM | for any element in a key, remove a specified number of those elements (the count)
@route('/lists/remove/', method='POST')
@view('central')
def template_lists_lrem():
    key = request.POST.get('key', '').strip()
    count= request.POST.get('count', '').strip()
    element = request.POST.get('element', '').strip()
    lrem = r.lrem(key, count, element)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, returned_value=lrem, db_size=db_size, search_result=search_result, info=info)



# LPOP | return and remove the first element of a list
@route('/lists/leftpop/', method='POST')
@view('central')
def template_lists_lpop():
    key = request.POST.get('key', '').strip()
    left_pop = r.lpop(key)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=left_pop, db_size=db_size, search_result=search_result, info=info)


# RPOP | return and remove the last element of a list
@route('/lists/rightpop/', method='POST')
@view('central')
def template_lists_rpop():
    key = request.POST.get('key', '').strip()
    right_pop = r.rpop(key)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=right_pop, db_size=db_size, search_result=search_result, info=info)

"""
These features are only in the Git edge versions of Redis -- you can activate the features if you are using
Redis version 1.3.1 or greater

# BLPOP
@route('/lists/blpop/', method='POST')
@view('central')
def template_lists_blpop():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    blpop = r.blpop(tuple_keys)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=blpop, db_size=db_size, search_result=search_result, info=info)


# BRPOP
@route('/lists/brpop/', method='POST')
@view('central')
def template_lists_blrop():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    brpop = r.brpop(tuple_keys)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=brpop, db_size=db_size, search_result=search_result, info=info)

# RPOPLPPUSH
"""

### Sets ###


# SADD | add a member to a set
@route('/sets/add/', method='POST')
@view('central')
def template_sets_add():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    set_add = r.sadd(key, member)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, member=member, returned_value=set_add, db_size=db_size, search_result=search_result, info=info)      


# SREM | remove a member of a set
@route('/sets/remove/', method='POST')
@view('central')
def template_sets_remove():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    set_remove = r.srem(key, member)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, member=member, returned_value=set_remove, db_size=db_size, search_result=search_result, info=info)      


# SPOP | return and remove a random member from a set
@route('/sets/pop/', method='POST')
@view('central')
def template_sets_pop():
    key = request.POST.get('key', '').strip()
    random_pop = r.spop(key)
    db_size = r.dbsize()  
    info = r.info()
  
    return dict(key=key, returned_value=random_pop, db_size=db_size, search_result=search_result, info=info)      

# SMOVE | move a member of a one set to another set
@route('/sets/move/', method='POST')
@view('central')
def template_sets_move():
    source_key = request.POST.get('source_key', '').strip()
    destination_key = request.POST.get('destination_key', '').strip()
    member = request.POST.get('member', '').strip()
    smove = r.smove(source_key, destination_key, member)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(member=member, returned_value=smove, db_size=db_size, search_result=search_result, info=info)      


# SCARD | return the cardinality for a set
@route('/sets/cardinality/', method='POST')
@view('central')
def template_sets_cardinality():
    key = request.POST.get('key', '').strip() 
    cardinality = r.scard(key)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=cardinality, db_size=db_size, search_result=search_result, info=info)


# SISMEMBER | check if a member is stored at a key - returns 1 if true, 0 if false
@route('/sets/ismember/', method='POST')
@view('central')
def template_sets_ismember():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    is_member = r.sismember(key, member)
    db_size = r.dbsize()  
    info = r.info()
 
    return dict(key=key, member=member, returned_value=is_member, db_size=db_size, search_result=search_result, info=info)      


# SINTER | for any number of sets, return the intersection
@route('/sets/intersection/', method='POST')
@view('central')
def template_sets_intersection():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    intersection = r.sinter(tuple_keys)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=intersection, db_size=db_size, search_result=search_result, info=info)


# SINTERSTORE | for any number of sets, return the intersection and store it as a new key
@route('/sets/interstore/', method='POST')
@view('central')
def template_sets_interstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    interstore = r.sinterstore(destination_key, tuple_keys)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=interstore, db_size=db_size, search_result=search_result, info=info)


# SUNION | for any number of sets, return the union
@route('/sets/union/', method='POST')
@view('central')
def template_sets_union():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    union = r.sunion(tuple_keys)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=union, db_size=db_size, search_result=search_result, info=info)


# SUNIONSTORE | for any number of sets, return the union and store it as a new key
@route('/sets/unionstore/', method='POST')
@view('central')
def template_sets_unionstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    unionstore = r.sunionstore(destination_key, tuple_keys)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=unionstore, db_size=db_size, search_result=search_result, info=info)


# SDIFF | for any number of sets, return the difference
@route('/sets/difference/', method='POST')
@view('central')
def template_sets_difference():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    difference = r.sunion(tuple_keys)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=difference, db_size=db_size, search_result=search_result, info=info)


# SDIFFSTORE | for any number of sets, return the difference and store it as a new key
@route('/sets/diffstore/', method='POST')
@view('central')
def template_sets_diffstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    diffstore = r.sdiffstore(destination_key, tuple_keys)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=diffstore, db_size=db_size, search_result=search_result, info=info)


# SMEMBERS | return all members of a set
@route('/sets/members/', method='POST')
@view('central')
def template_sets_members():
    key = request.POST.get('key', '').strip()
    members = r.smembers(key)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=members, db_size=db_size, search_result=search_result, info=info)


# SRANDMEMBER | return a random member of set, without removing it
@route('/sets/random/', method='POST')
@view('central')
def template_sets_srandom():
    key = request.POST.get('key', '').strip()
    random_member = r.srandmember(key)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=random_member, db_size=db_size, search_result=search_result, info=info)


### Sorted Sets ###


# ZADD | add a member to a sorted set
@route('/zsets/add/', method='POST')
@view('central')
def template_zsets_add():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    score = request.POST.get('score', '').strip()
    zset_add = r.zadd(key, member, score)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, member=member, score=score, returned_value=zset_add, db_size=db_size, search_result=search_result, info=info)      


# ZREM | remove a member of a sorted set
@route('/zsets/remove/', method='POST')
@view('central')
def template_zsets_remove():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    zset_remove = r.zrem(key, member)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, member=member, returned_value=zset_remove, db_size=db_size, search_result=search_result, info=info)      


# ZINCRBY | increment a member by any amount
@route('/zsets/incrementby/', method='POST')
@view('central')
def template_zsets_incrementby():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    amount = request.POST.get('amount', '').strip()
    incrementby = r.zincr(key, member, amount)
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=incrementby, db_size=db_size, search_result=search_result, info=info)	


# ZRANGE  return a range
@route('/zsets/range/', method='POST')
@view('central')
def template_zsets_zrange():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    zrange = r.zrange(key, start, end, desc=False, withscores=False)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=zrange, db_size=db_size, search_result=search_result, info=info)


@route('/zsets/rangewithscores/', method='POST')
@view('central')
def template_zsets_zrangewithscores():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    zrange = r.zrange(key, start, end, desc=False, withscores=True)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=zrange, db_size=db_size, search_result=search_result, info=info)


# ZRANGEBYSCORE | range by score
@route('/zsets/rangebyscore/', method='POST')
@view('central')
def template_rangebyscore():
    key = request.POST.get('key', '').strip()
    minimum = request.POST.get('min', '').strip()
    maximum = request.POST.get('max', '').strip()
    zrange = r.zrangebyscore(key, minimum, maximum, withscores=False)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=zrange, db_size=db_size, search_result=search_result, info=info)     


# ZREVRANGE | return a range in reverse order
@route('/zsets/revrange/', method='POST')
@view('central')
def template_zsets_zrevrange():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    zrevrange = r.zrevrange(key, start, end, withscores=False)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=zrevrange, db_size=db_size, search_result=search_result, info=info)


# ZREVRANGE | return a range in reverse order, with scores
@route('/zsets/revrangewithscores/', method='POST')
@view('central')
def template_zsets_zrevrangescores():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    zrevrange = r.zrevrange(key, start, end, withscores=True)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=zrevrange, db_size=db_size, search_result=search_result, info=info)


# ZCARD | return the cardinality for a set
@route('/zsets/cardinality/', method='POST')
@view('central')
def template_zsets_cardinality():
    key = request.POST.get('key', '').strip() 
    cardinality = r.zcard(key)
    db_size = r.dbsize()
    info = r.info()

    return dict(key=key, returned_value=cardinality, db_size=db_size, search_result=search_result, info=info)


# ZSCORE | return the score for a particular key and member
@route('/zsets/score/', method='POST')
@view('central')
def template_zsets_score():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    score = r.zscore(key, member)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, member=member, returned_value=score, db_size=db_size, search_result=search_result, info=info)    


# ZREMRANGEBYSCORE
@route('/zsets/remrangebyscore/', method='POST')
@view('central')
def template_zremrangebyscore():
    key = request.POST.get('key', '').strip()
    minimum = request.POST.get('min', '').strip()
    maximum = request.POST.get('max', '').strip()
    remrange = r.zremrangebyscore(key, minimum, maximum)
    db_size = r.dbsize()
    info = r.info()
  
    return dict(key=key, returned_value=remrange, db_size=db_size, search_result=search_result, info=info)    

### Hashes ###

# HSET | Set the hash field to the specified value. Creates the hash if needed.
@route('/hashes/hset/', method='POST')
@view('central')
def template_hashes_set():
    key = request.POST.get('key', '').strip()
    field = request.POST.get('field', '').strip()
    value = request.POST.get('value', '').strip()
    hset = r.hset(key, field, value)
    db_size = r.dbsize()
    info = r.info()
 
    return dict(key=key, value=value, returned_value=hset, db_size=db_size, search_result=search_result, info=info)

# HGET | return the string value of a key
@route('/hashes/get/', method='POST')
@view('central')
def template_hashes_get():
    key = request.POST.get('key', '').strip()
    field = request.POST.get('field', '').strip()
    hget = r.hget(key, field)	
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=hget, db_size=db_size, search_result=search_result, info=info)	

# HDEL | Remove the specified field from a hash
@route('/hashes/delete/', method='POST')
@view('central')
def template_hashes_delete():
    key = request.POST.get('key', '').strip()
    field = request.POST.get('field', '').strip()
    hdel = r.hdel(key, field)	
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=hdel, db_size=db_size, search_result=search_result, info=info)	

# HEXIST | Test if the specified field exists in a hash
@route('/hashes/exists/', method='POST')
@view('central')
def template_hashes_exists():
    key = request.POST.get('key', '').strip()
    field = request.POST.get('field', '').strip()
    hexists = r.hexists(key, field)	
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=hexists, db_size=db_size, search_result=search_result, info=info)	

# HLEN | Return the number of fields contained in a hash
@route('/hashes/length/', method='POST')
@view('central')
def template_hashes_length():
    key = request.POST.get('key', '').strip()
    hlen = r.hlen(key)	
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=hlen, db_size=db_size, search_result=search_result, info=info)	

# HKEYS | Return all the fields names contained into a hash
@route('/hashes/keys/', method='POST')
@view('central')
def template_hashes_keys():
    key = request.POST.get('key', '').strip()
    hkeys = r.hkeys(key)	
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=hkeys, db_size=db_size, search_result=search_result, info=info)	

# HVALS | Return all the values contained into a hash
@route('/hashes/values/', method='POST')
@view('central')
def template_hashes_values():
    key = request.POST.get('key', '').strip()
    hvals = r.hvals(key)	
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=hvals, db_size=db_size, search_result=search_result, info=info)	

# HGETALL | Return both the fields names and the values contained into a hash
@route('/hashes/getall/', method='POST')
@view('central')
def template_string_get():
    key = request.POST.get('key', '').strip()
    hgetall = r.hgetall(key)	
    db_size = r.dbsize()
    info = r.info()
	
    return dict(key=key, returned_value=hgetall, db_size=db_size, search_result=search_result, info=info)	

### Server ###

# SAVE | save the DB to disk
@route('/save/', method='POST')
@view('central')
def template_save():
    save = r.save()
    info = r.info()
    db_size = r.dbsize()

    return dict(returned_value=save, db_size=db_size, search_result=search_result, info=info)


# BGSAVE | save the data to disk -- asynchronous 
@route('/bgsave/', method='POST')
@view('central')
def template_bgsave():
    bgsave = r.bgsave()
    info = r.info()
    db_size = r.dbsize()

    return dict(returned_value=bgsave, db_size=db_size, search_result=search_result, info=info)


# LASTSAVE | return the time of the last save
@route('/lastsave/', method='POST')
@view('central')
def template_lastsave():
    lastsave = r.lastsave()
    info = r.info()
    db_size = r.dbsize()

    return dict(returned_value=lastsave, db_size=db_size, search_result=search_result, info=info)


# INFO
@route('/info/', method='POST')
@view('central')
def template_info():
    db_size = r.dbsize()  
    info = r.info()  
  
    return dict(returned_value=returned_value, db_size=db_size, search_result=search_result, info=info)    


#run it!
run()
