"""
Redweb is a web interface to the Redis key-value store and server. It is writte
n in Python, and is built on the Bottle micro-framework. With Redweb, you 
can easily interact with the Redis database through your
web browser, utilizing POST functionality.

  28 Mar 2010 | Adding hash functions (thanks gnrfan) (0.2.3)
  15 Mar 2010 | Additional ZSET functionality
  13 Mar 2010 | Save and background save functionality added (0.2.1)         
  28 Feb 2010 | Redweb requires refactored redis-py bindings (0.2.0)
   8 Feb 2010 | all functions return either a status code, value, etc. (0.1.1)
   5 Feb 2010 | additional set functionality, UI improvements
   2 Feb 2010 | first public release (0.1.0)
"""

__author__ = 'Ted Nyman'
__version__ = '0.2.3'
__license__ = 'MIT'


from bottle import route, request, response, view, static_file, run
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

# function for set connection status (infoAboutConnection)
def setGlobalConnectionStatus():
    if hasattr(r, "host"):
        infoAboutConnection['host'] = r.host
        infoAboutConnection['port'] = r.port
        infoAboutConnection['db'] = r.db
    else:
        connection = r.connection_pool.get_connection('info')
        infoAboutConnection['host'] = connection.host
        infoAboutConnection['port'] = connection.port
        infoAboutConnection['db'] = connection.db
        connection.disconnect()
        
# infoAboutConnection defaults to empty dict  
infoAboutConnection = {}
setGlobalConnectionStatus()
    
def dictWithAddedCommonFields(**kwargs):
    kwargs.update({'db_size':r.dbsize(),'info':r.info(),'search_result':search_result,'infoAboutConnection':infoAboutConnection})
    return kwargs



# Set static file routing
@route('/static/:filename')
def send_file(filename):
    return static_file(filename, root='../redweb/static')

# Home route
@route('/')
@view('central')
def template_keyvalue():
   return dictWithAddedCommonFields(returned_value=returned_value)
               
### Settings for DB ###
@route('/settings/db', method='POST')
def template_settings():
    host = request.POST.get('host', '')
    port = int(request.POST.get('port', 6379))
    dbnum = int(request.POST.get('dbnum', 0))
    
    global r
    r = redis.Redis(host=host, port=port, db=dbnum)     
    returned_value = True
    setGlobalConnectionStatus()    
    return dictWithAddedCommonFields(returned_value=returned_value)

### Actions for all data types ###
 
@route('/delete', method='POST')
def template_delete():
    key_delete = request.POST.get('key_delete', '').strip()
    delete = r.delete(key_delete)
    
    return dictWithAddedCommonFields(returned_value=delete)

@route('/delete/all', method='POST')
def template_delete_all():
    delete_all = request.POST.get('delete_all', '').strip()
    r.flushdb()

    return dictWithAddedCommonFields(search_result=search_result)

@route('/search', method='POST')
def template_search():
    key = request.POST.get('key', '').strip()
    search_result = r.keys(key)

    return dictWithAddedCommonFields(returned_value=search_result)

### Strings ###

# SET | set a string value for a given key
@route('/strings/set', method='POST')
def template_strings_set():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()
    sset = r.set(key,value)
 
    return dictWithAddedCommonFields(key=key, value=value, returned_value=sset)


# GET | return the string value of a key
@route('/strings/get', method='POST')
def template_string_get():
    key = request.POST.get('key', '').strip()
    get = r.get(key)    
    
    return dictWithAddedCommonFields(key=key, returned_value=get)    

# GETSET | set a string value for a key, only if the key does not exist, 
# and return value
@route('/strings/getset', method='POST')
def template_strings_getset():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()
    getset = r.getset(key,value)
 
    return dictWithAddedCommonFields(key=key, value=value, returned_value=getset)

# MGET

# SETNX | set a string value for a given key, only if the key does not exists
@route('/strings/setnx', method='POST')
def template_strings_setnx():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()
    setnx = r.setnx(key,value)
 
    return dictWithAddedCommonFields(key=key, value=value, returned_value=setnx)

# MSET
# MSETNX

# INCR | increment a value by 1
@route('/strings/increment', method='POST')
def template_string_increment():
    key = request.POST.get('key', '').strip()
    increment = r.incr(key)
    
    return dictWithAddedCommonFields(key=key, returned_value=increment)    


# INCRBY | increment a value by any amount
@route('/strings/incrementby', method='POST')
def template_string_incrementby():
    key = request.POST.get('key', '').strip()
    amount = request.POST.get('amount', '').strip()
    incrementby = r.incr(key, amount)
    
    return dictWithAddedCommonFields(key=key, returned_value=incrementby)    

# DECR | decrement a value by 1
@route('/strings/decrement', method='POST')
def template_string_decrement():
    key = request.POST.get('key', '').strip()
    decrement = r.decr(key)
    
    return dictWithAddedCommonFields(key=key, returned_value=decrement)    

# DECRBY | decrement a value by any amount
@route('/strings/decrementby', method='POST')
def template_string_decrementby():
    key = request.POST.get('key', '').strip()
    amount = request.POST.get('amount', '').strip()
    decrementby = r.decr(key, amount)
    
    return dictWithAddedCommonFields(key=key, returned_value=decrementby)    

### Lists ###

# RPUSH | append an element to the tail of a list
@route('/lists/rightpush', method='POST')
def template_lists_rightpush():
    key = request.POST.get('key', '').strip()
    element = request.POST.get('element', '').strip()
    right_push = r.rpush(key,element)
 
    return dictWithAddedCommonFields(key=key, element=element, returned_value=right_push)

# LPUSH | append an element to the head of a list
@route('/lists/leftpush', method='POST')
def template_lists_leftpush():
    key = request.POST.get('key', '').strip()
    element = request.POST.get('element', '').strip()
    left_push = r.lpush(key,element)

    return dictWithAddedCommonFields(key=key, element=element, returned_value=left_push)

# LLEN | return the length of a list
@route('/lists/length', method='POST')
def template_lists_length():
    key = request.POST.get('key', '').strip()
    llen = r.llen(key)

    return dictWithAddedCommonFields(key=key, returned_value=llen)

# LRANGE | return a range of elements from a list
@route('/lists/range', method='POST')
def template_lists_range():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    list_range = r.lrange(key, start, end)

    return dictWithAddedCommonFields(key=key, returned_value=list_range)

# LTRIM | trim a list so that it contains just the specific range of elements
@route('/lists/trim', method='POST')
def template_lists_range():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    ltrim = r.ltrim(key, start, end)

    return dictWithAddedCommonFields(key=key, returned_value=ltrim)

# LINDEX | return the indexed element for a particular key
@route('/lists/lindex', method='POST')
def template_lists_lindex():
    key = request.POST.get('key', '').strip()
    index = request.POST.get('index', '').strip()
    list_index = r.lindex(key, index)
 
    return dictWithAddedCommonFields(key=key, returned_value=list_index)

# LSET | set the list element at index
@route('/lists/set', method='POST')
def template_lists_lset():
    key = request.POST.get('key', '').strip()
    index = request.POST.get('index', '').strip()
    element = request.POST.get('element', '').strip()
    lset = r.lset(key, index, element)
 
    return dictWithAddedCommonFields(key=key, returned_value=lset)

# LREM | for any element in a key, remove a specified number of those 
# elements (the count)
@route('/lists/remove', method='POST')
def template_lists_lrem():
    key = request.POST.get('key', '').strip()
    count= request.POST.get('count', '').strip()
    element = request.POST.get('element', '').strip()
    lrem = r.lrem(key, count, element)
 
    return dictWithAddedCommonFields(key=key, returned_value=lrem)

# LPOP | return and remove the first element of a list
@route('/lists/leftpop', method='POST')
def template_lists_lpop():
    key = request.POST.get('key', '').strip()
    left_pop = r.lpop(key)

    return dictWithAddedCommonFields(key=key, returned_value=left_pop)

# RPOP | return and remove the last element of a list
@route('/lists/rightpop', method='POST')
def template_lists_rpop():
    key = request.POST.get('key', '').strip()
    right_pop = r.rpop(key)

    return dictWithAddedCommonFields(key=key, returned_value=right_pop)

# BLPOP
@route('/lists/blpop', method='POST')
def template_lists_blpop():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    blpop = r.blpop(tuple_keys)

    return dictWithAddedCommonFields(key=key, returned_value=blpop)

# BRPOP
@route('/lists/brpop', method='POST')
def template_lists_blrop():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    brpop = r.brpop(tuple_keys)

    return dictWithAddedCommonFields(key=key, returned_value=brpop)

# RPOPLPPUSH

### Sets ###

# SADD | add a member to a set
@route('/sets/add', method='POST')
def template_sets_add():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    set_add = r.sadd(key, member)

    return dictWithAddedCommonFields(key=key, member=member, returned_value=set_add)      

# SREM | remove a member of a set
@route('/sets/remove', method='POST')
def template_sets_remove():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    set_remove = r.srem(key, member)
 
    return dictWithAddedCommonFields(key=key, member=member, returned_value=set_remove)      

# SPOP | return and remove a random member from a set
@route('/sets/pop', method='POST')
def template_sets_pop():
    key = request.POST.get('key', '').strip()
    random_pop = r.spop(key)
  
    return dictWithAddedCommonFields(key=key, returned_value=random_pop)      

# SMOVE | move a member of a one set to another set
@route('/sets/move', method='POST')
def template_sets_move():
    source_key = request.POST.get('source_key', '').strip()
    destination_key = request.POST.get('destination_key', '').strip()
    member = request.POST.get('member', '').strip()
    smove = r.smove(source_key, destination_key, member)
 
    return dictWithAddedCommonFields(member=member, returned_value=smove)      

# SCARD | return the cardinality for a set
@route('/sets/cardinality', method='POST')
def template_sets_cardinality():
    key = request.POST.get('key', '').strip() 
    cardinality = r.scard(key)

    return dictWithAddedCommonFields(key=key, returned_value=cardinality)

# SISMEMBER | check if a member is stored at a key - returns 1 if true, 
# or 0 if false
@route('/sets/ismember', method='POST')
def template_sets_ismember():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    is_member = r.sismember(key, member)
 
    return dictWithAddedCommonFields(key=key, member=member, returned_value=is_member)      

# SINTER | for any number of sets, return the intersection
@route('/sets/intersection', method='POST')
def template_sets_intersection():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    intersection = r.sinter(tuple_keys)
  
    return dictWithAddedCommonFields(key=key, returned_value=intersection)

# SINTERSTORE | for any number of sets, return the intersection and store 
# it as a new key
@route('/sets/interstore', method='POST')
def template_sets_interstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    interstore = r.sinterstore(destination_key, tuple_keys)
  
    return dictWithAddedCommonFields(key=key, returned_value=interstore)

# SUNION | for any number of sets, return the union
@route('/sets/union', method='POST')
def template_sets_union():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    union = r.sunion(tuple_keys)
  
    return dictWithAddedCommonFields(key=key, returned_value=union)

# SUNIONSTORE | for any number of sets, return the union and store it 
# as a new key
@route('/sets/unionstore', method='POST')
def template_sets_unionstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    unionstore = r.sunionstore(destination_key, tuple_keys)
  
    return dictWithAddedCommonFields(key=key, returned_value=unionstore)

# SDIFF | for any number of sets, return the difference
@route('/sets/difference', method='POST')
def template_sets_difference():
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    difference = r.sunion(tuple_keys)
  
    return dictWithAddedCommonFields(key=key, returned_value=difference)

# SDIFFSTORE | for any number of sets, return the difference and store it as a new key
@route('/sets/diffstore', method='POST')
def template_sets_diffstore():
    destination_key = request.POST.get('destkey', '').strip()
    key = request.POST.get('key', '').strip()
    keys = string.split(key, ',')
    tuple_keys = tuple(keys)
    diffstore = r.sdiffstore(destination_key, tuple_keys)
  
    return dictWithAddedCommonFields(key=key, returned_value=diffstore)

# SMEMBERS | return all members of a set
@route('/sets/members', method='POST')
def template_sets_members():
    key = request.POST.get('key', '').strip()
    members = r.smembers(key)
  
    return dictWithAddedCommonFields(key=key, returned_value=members)

# SRANDMEMBER | return a random member of set, without removing it
@route('/sets/random', method='POST')
def template_sets_srandom():
    key = request.POST.get('key', '').strip()
    random_member = r.srandmember(key)
  
    return dictWithAddedCommonFields(key=key, returned_value=random_member)

### Sorted Sets ###

# ZADD | add a member to a sorted set
@route('/zsets/add', method='POST')
def template_zsets_add():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    score = request.POST.get('score', '').strip()
    zset_add = r.zadd(key, member, score)
 
    return dictWithAddedCommonFields(key=key, member=member, score=score, returned_value=zset_add)      

# ZREM | remove a member of a sorted set
@route('/zsets/remove', method='POST')
def template_zsets_remove():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    zset_remove = r.zrem(key, member)

    return dictWithAddedCommonFields(key=key, member=member, returned_value=zset_remove)      

# ZINCRBY | increment a member by any amount
@route('/zsets/incrementby', method='POST')
def template_zsets_incrementby():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    amount = request.POST.get('amount', '').strip()
    incrementby = r.zincr(key, member, amount)
    
    return dictWithAddedCommonFields(key=key, returned_value=incrementby)    

# ZRANGE  return a range
@route('/zsets/range', method='POST')
def template_zsets_zrange():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    zrange = r.zrange(key, start, end, desc=False, withscores=False)

    return dictWithAddedCommonFields(key=key, returned_value=zrange)

@route('/zsets/rangewithscores', method='POST')
def template_zsets_zrangewithscores():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    zrange = r.zrange(key, start, end, desc=False, withscores=True)

    return dictWithAddedCommonFields(key=key, returned_value=zrange)

# ZRANGEBYSCORE | range by score
@route('/zsets/rangebyscore', method='POST')
def template_rangebyscore():
    key = request.POST.get('key', '').strip()
    minimum = request.POST.get('min', '').strip()
    maximum = request.POST.get('max', '').strip()
    zrange = r.zrangebyscore(key, minimum, maximum, withscores=False)
  
    return dictWithAddedCommonFields(key=key, returned_value=zrange)     

# ZREVRANGE | return a range in reverse order
@route('/zsets/revrange', method='POST')
def template_zsets_zrevrange():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    zrevrange = r.zrevrange(key, start, end, withscores=False)

    return dictWithAddedCommonFields(key=key, returned_value=zrevrange)

# ZREVRANGE | return a range in reverse order, with scores
@route('/zsets/revrangewithscores', method='POST')
def template_zsets_zrevrangescores():
    key = request.POST.get('key', '').strip()
    start = request.POST.get('start', '').strip()
    end = request.POST.get('end', '').strip()
    zrevrange = r.zrevrange(key, start, end, withscores=True)

    return dictWithAddedCommonFields(key=key, returned_value=zrevrange)

# ZCARD | return the cardinality for a set
@route('/zsets/cardinality', method='POST')
def template_zsets_cardinality():
    key = request.POST.get('key', '').strip() 
    cardinality = r.zcard(key)

    return dictWithAddedCommonFields(key=key, returned_value=cardinality)

# ZSCORE | return the score for a particular key and member
@route('/zsets/score', method='POST')
def template_zsets_score():
    key = request.POST.get('key', '').strip()
    member = request.POST.get('member', '').strip()
    score = r.zscore(key, member)
  
    return dictWithAddedCommonFields(key=key, member=member, returned_value=score)    

# ZREMRANGEBYSCORE
@route('/zsets/remrangebyscore', method='POST')
def template_zsets_remrangebyscore():
    key = request.POST.get('key', '').strip()
    minimum = request.POST.get('min', '').strip()
    maximum = request.POST.get('max', '').strip()
    remrange = r.zremrangebyscore(key, minimum, maximum)
  
    return dictWithAddedCommonFields(key=key, returned_value=remrange)    

### Hashes ###

# HSET | Set the hash field to the specified value. Creates the hash if needed.
@route('/hashes/hset', method='POST')
def template_hashes_set():
    key = request.POST.get('key', '').strip()
    field = request.POST.get('field', '').strip()
    value = request.POST.get('value', '').strip()
    hset = r.hset(key, field, value)
 
    return dictWithAddedCommonFields(key=key, value=value, returned_value=hset)

# HGET | return the string value of a key
@route('/hashes/get', method='POST')
def template_hashes_get():
    key = request.POST.get('key', '').strip()
    field = request.POST.get('field', '').strip()
    hget = r.hget(key, field)    
    
    return dictWithAddedCommonFields(key=key, returned_value=hget)    

# HDEL | Remove the specified field from a hash
@route('/hashes/delete', method='POST')
def template_hashes_delete():
    key = request.POST.get('key', '').strip()
    field = request.POST.get('field', '').strip()
    hdel = r.hdel(key, field)    
    
    return dictWithAddedCommonFields(key=key, returned_value=hdel)    

# HEXIST | Test if the specified field exists in a hash
@route('/hashes/exists', method='POST')
def template_hashes_exists():
    key = request.POST.get('key', '').strip()
    field = request.POST.get('field', '').strip()
    hexists = r.hexists(key, field)    
    
    return dictWithAddedCommonFields(key=key, returned_value=hexists)    

# HLEN | Return the number of fields contained in a hash
@route('/hashes/length', method='POST')
def template_hashes_length():
    key = request.POST.get('key', '').strip()
    hlen = r.hlen(key)    
    
    return dictWithAddedCommonFields(key=key, returned_value=hlen)    

# HKEYS | Return all the fields names contained into a hash
@route('/hashes/keys', method='POST')
def template_hashes_keys():
    key = request.POST.get('key', '').strip()
    hkeys = r.hkeys(key)    

    return dictWithAddedCommonFields(key=key, returned_value=hkeys)    

# HVALS | Return all the values contained into a hash
@route('/hashes/values', method='POST')
def template_hashes_values():
    key = request.POST.get('key', '').strip()
    hvals = r.hvals(key)    
    
    return dictWithAddedCommonFields(key=key, returned_value=hvals)    

# HGETALL | Return both the fields names and the values contained into a hash
@route('/hashes/getall', method='POST')
def template_hashes_getall():
    key = request.POST.get('key', '').strip()
    hgetall = r.hgetall(key)    
    
    return dictWithAddedCommonFields(key=key, returned_value=hgetall)    

### Server ###

# SAVE | save the DB to disk
@route('/save', method='POST')
def template_save():
    save = r.save()

    return dictWithAddedCommonFields(returned_value=save)

# BGSAVE | save the data to disk -- asynchronous 
@route('/bgsave', method='POST')
def template_bgsave():
    bgsave = r.bgsave()

    return dictWithAddedCommonFields(returned_value=bgsave)

# LASTSAVE | return the time of the last save
@route('/lastsave', method='POST')
def template_lastsave():
    lastsave = str(r.lastsave())

    return dictWithAddedCommonFields(returned_value=lastsave)

# INFO
@route('/info', method='POST')
def template_info():
  
    return dictWithAddedCommonFields(returned_value=returned_value)    


class StripPathMiddleware(object):
  def __init__(self, app):
    self.app = app
  def __call__(self, e, h):
    e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
    return self.app(e,h)

app = bottle.default_app()
app = StripPathMiddleware(app)
bottle.run(app=app)