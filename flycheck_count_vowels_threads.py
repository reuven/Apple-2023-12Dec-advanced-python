#!/usr/bin/env python3

import threading
from queue import Queue
import glob

q = Queue()

def count_vowels(filename):
    # counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    counts = dict.fromkeys('aeiou', 0)

    for one_line in open(filename):
        for one_character in one_line:
            if one_character in output:
                counts[one_character] += 1

    q.put((filename, counts))

for one_filename in glob.glob('/etc/*.conf'):
    t = threading.Thread(target=count_vowels, args=(one_filename,))
    t.start()

# wait for the threads to finish
while threading.active_count() > 1:
    for one_thread in threading.enumerate():
        if one_thread != threading.current_thread():
            one_thread.join(0.0001)  # timeout is 0.0001 sec

print('Done!')

while not q.empty():
    filename, 

    print(q.get())
