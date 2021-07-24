from __future__ import (absolute_import, division, print_function,unicode_literals)

from rq import Connection, Queue, Worker
from redis import Redis

redis = Redis(host='redis')
if __name__ == '__main__':
    with Connection(connection=redis):
        q = Queue()
        Worker(q).work()