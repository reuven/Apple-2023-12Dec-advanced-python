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
        return filename, f'[Error reading from file {filename}]'

    return filename, output

with ThreadPoolExecutor() as executor:
    results = executor.map(longest_word,
                           glob.glob('/etc/*.conf'))

    for filename, one_result in results:
        print(f'{filename}: {one_result.strip()}')
