from lock import Lock
from drivers.redis_driver import RedisDriver

result = lock = Lock(RedisDriver(host="127.0.0.1"), "lock", tries=5, delay=10)
with lock:
    print("hello world!")
print("bye bye world")
