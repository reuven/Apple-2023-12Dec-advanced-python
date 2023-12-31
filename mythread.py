#!/usr/bin/env python3

import threading
import time
import random

def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!')

all_threads = []
for i in range(10):
    t = threading.Thread(target=hello, args=(i,))
    all_threads.append(t)
    t.start()

# "join" on a thread means: wait until it's done
for one_thread in all_threads:
    one_thread.join()

print('Done!')
