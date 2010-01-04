from bottle import route, view, run
import redis

r = redis.Redis()


@route('/keyvalue/:key/:value/add')
@view('add')

def template_add(key,value):
	key = key.strip()
	value = value.strip()
	
	r.set(key, value)

	return dict(title="Key-Value Pair with Redis", key=key, value=value)


@route('keyvalue/:key/:value/delete')
@view('delete')

def template_delete(key,value):
        key = key.strip()
        value = value.strip()
	
	r.delete(key)

        return dict(title="Key-Value Pair with Redis", key=key, value=value)


@route('keyvalue/:key/')
@view('show')

def template_show(key):
	the_key = key.strip()
	value = r.get(the_key)	
	
	return dict(title=the_key, the_key=the_key, value=value)	
run()
