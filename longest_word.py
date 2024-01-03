#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
import glob

def longest_word(filename):
    output = ''

    try:
        for one_line in open(filename):
            for one_word in one_line.split():
                if len(one_word) > len(output):
                    output = one_word
    except Exception as e:
        print(f'\tError reading from file {filename}')

    return output

with ThreadPoolExecutor() as executor:
    results = executor.map(longest_word, glob.glob('/etc/*.conf'))
