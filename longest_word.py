#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor

def longest_word(filename):
    output = ''

    try:
        for one_line in open(filename):
            for one_word in one_line.split():
                if len(one_word) > output:
                    output = one_word

    return output
