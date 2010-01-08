__author__ = 'Ted Nyman'
__version__ = '0.1.0'
__license__ = 'MIT'

from bottle import route, request, response, view, send_file, run
import redis
import bottle

r = redis.Redis()

@route('/static/:filename')
def static_file(filename):
    send_file(filename, root='../redbottle/static')

@route('/keyvalue/')
@view('keys')
def template_keyvalue():   
    all_keys = r.keys('*')
    db_size = r.dbsize()
    return dict(title='Key-Value Store', db_size=db_size, all_keys=all_keys)

@route('/keyvalue/add/', method='POST')
@view('keys')
def template_add():
    key = request.POST.get('key', '').strip()
    value = request.POST.get('value', '').strip()

    r.set(key,value)
    all_keys = r.keys('*')
    db_size = r.dbsize()
 
    return dict(title="Key-Value Pair", key=key, db_size=db_size, value=value, all_keys=all_keys)

@route('/keyvalue/delete/', method='POST')
@view('keys')
def template_delete():

    key_delete = request.POST.get('key_delete', '').strip()
    r.delete(key_delete)
    all_keys = r.keys('*')
    db_size = r.dbsize()	
	   
    return dict(title="Key-Value Pair", db_size = db_size, key=key_delete, all_keys=all_keys)

@route('keyvalue/show/:key')
@view('show')

def template_show(key):
    key = key
    value = r.get(key)	
	
    return dict(title=key, key=key, value=value)	

run()
