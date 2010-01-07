from bottle import route, request, response, view, send_file, run
import redis

r = redis.Redis()

@route('/static/:filename')
def static_file(filename):
	send_file(filename, root='../redbottle/static')

@route('/keyvalue/')
@view('keys')
def template_keyvalue():

	all_keys = r.keys('*')
	return dict(title='Key-Value Store', all_keys=all_keys)

@route('/keyvalue/add/', method='POST')
@view('keys')
def template_add():

	if 'key' in request.POST and 'value' in request.POST:
		key = request.POST['key']
		value = request.POST['value']

	r.set(key,value)
	all_keys = r.keys('*')
	return dict(title="Key-Value Pair", key=key, value=value, all_keys=all_keys)

@route('/keyvalue/delete/', method='POST')
@view('keys')
def template_delete():

        if 'key_delete' in request.POST:
                key_delete = request.POST['key_delete']

        r.delete(key_delete)
	all_keys = r.keys('*')
        return dict(title="Key-Value Pair", key=key_delete, all_keys=all_keys)

@route('keyvalue/show/:key')
@view('show')

def template_show(key):
	the_key = key.strip()
	value = r.get(the_key)	
	
	return dict(title=the_key, the_key=the_key, value=value)	
run()
