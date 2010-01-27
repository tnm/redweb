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

# Redis string functionality 

@route('/strings/')
@view('keys')
def template_keyvalue():  
    db_size = r.dbsize()
    return dict(title='Key-Value Store', db_size=db_size)

@route('/strings/add/', method='POST')
@view('keys')
def template_add():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()

    r.set(key,value)
    db_size = r.dbsize()
 
    return dict(title="Key-Value Pair", key=key, db_size=db_size, value=value)

@route('/strings/delete/', method='POST')
@view('keys')
def template_delete():

    key_delete = request.POST.get('key_delete', '').strip()
    r.delete(key_delete)
    db_size = r.dbsize()	
	   
    return dict(title="Key-Value Pair", db_size = db_size, key=key_delete)


@route('strings/show/:key')
@view('show')

def template_show(key):
    key = key
    value = r.get(key)	
	
    return dict(title=key, key=key, value=value)	


# Redis List Functionality

@route('/lists/')
@view('keys')
def template_keyvalue():  
    db_size = r.dbsize()
    return dict(title='Key-Value Store', db_size=db_size)

@route('/lists/push/', method='POST')
@view('keys')
def template_add():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()

    r.push(key,value)
    db_size = r.dbsize()
 
    return dict(title="Key-Value Pair", key=key, db_size=db_size, value=value)

@route('/lists/trim/', method='POST')
@view('keys')
def template_delete():

    key_delete = request.POST.get('key_delete', '').strip()
    r.delete(key_delete)
    db_size = r.dbsize()	
	   
    return dict(title="Key-Value Pair", db_size = db_size, key=key_delete)

@route('lists/show/:key')
@view('show')

def template_show(key):
    key = key
    value = r.get(key)	
	
    return dict(title=key, key=key, value=value)	





run()
