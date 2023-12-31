#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor
import glob
import time

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

if __name__ == '__main__':

    start_time = time.time()
    with ProcessPoolExecutor(max_workers=10) as executor:
        results = executor.map(longest_word,
                               glob.glob('/etc/*.conf'))

        end_time = time.time()
        total_time = end_time - start_time
        print(f'Total time: {total_time}')
        for filename, one_result in results:
            print(f'{filename}: {one_result.strip()}')
