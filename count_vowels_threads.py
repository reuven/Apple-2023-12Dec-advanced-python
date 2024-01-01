#!/usr/bin/env python3

import threading
from queue import Queue

q = Queue()

def count_vowels(filename):
    # output = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    output = dict.fromkeys('aeiou', 0)



# # Exercise: File vowels

# 1. Define a function, `count_vowels`, that takes a filename as an input. It uses `q.put` to return a tuple with two elements:
#     - the filename
#     - a dictionary with keys a, e, i, o, and u as an output. The values will be integers, the number of times each vowel appears in a file.
# 3. Use threads to start this function once per file in a directory (or a list of files that you provide). You can use `os.listdir` or `glob.glob`.
# 4. When all of the threads are done, go through the queue and print all of the filenames and the reports they've made.
# 5. If a file doesn't work (binary, no permission, etc.), then just ignore it.
