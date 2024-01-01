#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait
import glob

def count_vowels(filename):
    counts = dict.fromkeys('aeiou', 0)

    try:
        for one_line in open(filename):
            for one_character in one_line:
                if one_character in counts:
                    counts[one_character] += 1
        return filename, counts
    except Exception as e:
        print(f'\tError opening{filename}: {e}')

with ThreadPoolExecutor(max_workers=10) as executor:
    all_results = []
    for one_filename in glob.glob('/etc/*.conf'):
        one_result = executor.submit(count_vowels, one_filename)
        all_results.append(one_result)

    done, not_done = wait(all_results, return_when=FIRST_COMPLETED)

    for one_result in done:
        print(one_result.result())
