#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor

def count_vowels(filename):
    counts = dict.fromkeys('aeiou', 0)

    try:
        for one_line in open(filename):
            for one_character in one_line:
                if one_character in counts:
                    counts[one_character] += 1
        q.put((filename, counts))
    except Exception as e:
        print(f'\tError opening{filename}: {e}')
