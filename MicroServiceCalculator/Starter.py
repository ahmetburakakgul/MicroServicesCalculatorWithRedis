from __future__ import (absolute_import, division, print_function,unicode_literals)
import os
import time

from rq import Connection, Queue
from redis import Redis
from Calculate import calculate


def main():
    while True:
        redis = Redis(host='redis')
        problem = input("Problemi Girin : ")
        q = Queue(connection=redis)

        start_time = time.time()
        asycn_result = q.enqueue(calculate,problem)

        done = False
        while not done:
            os.system('clear')
            print('Asynchronously: (now = %.2f)' % (time.time() - start_time,))
            done = True
            job_result = asycn_result.return_value
            if job_result is None:
                done = False
                job_result = 'Hesaplanıyor'
            print('Sonuç = %s' % (job_result))
            time.sleep(0.2)

if __name__ == '__main__':
    with Connection():
        main()