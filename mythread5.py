#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def count_vowels(s):
    total = 0

    for one_character in s:
        if one_character in 'aeiou':
            total += 1

    return total

words = 'this is a fantastic and enticing and superfabulous sentence'.split()

if __name__ == '__main__':

    with ProcessPoolExecutor() as executor:
        # executor.__enter__()
        results = executor.map(count_vowels, words)

        for one_result in results:
            print(one_result)

        # executor.__exit__()
