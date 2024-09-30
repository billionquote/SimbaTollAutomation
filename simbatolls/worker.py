import os
import redis
# from redis import Redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDIS_URL');

# redis_url = os.getenv('REDIS_URL', 'rediss://:pf6c22c0fcedac7b44568fa823d496690a9624f061d7e1797f52d38f31d48294c@ec2-23-21-87-215.compute-1.amazonaws.com:12819')

conn = redis.from_url(redis_url, ssl_cert_reqs=None)
# conn = Redis(host='localhost', port=6379)
#conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
