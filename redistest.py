import redis

redis_test = redis.Redis()
redis_test.set('If you can see this', 'Redis is working')

