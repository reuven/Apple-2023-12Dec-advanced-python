#!/usr/bin/env python3

import threading
import time
import random

def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!')

for i in range(10):
    t = threading.Thread(target=hello, args=(i,))
    t.start()

# "join" on a thread means: wait until it's done
while threading.active_count() > 1:
    for one_thread in threading.enumerate():
        if one_thread != threading.current_thread():
            one_thread.join(0.1)

print('Done!')
