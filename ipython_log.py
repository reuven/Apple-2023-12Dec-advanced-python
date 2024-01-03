# IPython log file


# list comprehension

numbers = range(10)

[one_number ** 2
 for one_number in numbers]
numbers = range(10)

[one_number ** 2
 for one_number in numbers
 if one_number % 2]
# how does map work?

# we pass map two arguments:
# 1. a function that takes one argument
# 2. an iterable of data

words = 'this is a bunch of words'

map(len, words)
# how does map work?

# we pass map two arguments:
# 1. a function that takes one argument
# 2. an iterable of data

words = 'this is a bunch of words'

list(map(len, words))
# how does map work?

# we pass map two arguments:
# 1. a function that takes one argument
# 2. an iterable of data

words = 'this is a bunch of words'.split()

list(map(len, words))
def count_vowels(s):
    total = 0

    for one_character in s:
        if one_character in 'aeiou':
            total += 1

    return total

list(map(count_vowels, words))
def count_vowels(s):
    total = 0

    for one_character in s:
        if one_character in 'aeiou':
            total += 1

    return total

words = 'this is a fantastic and enticing and superfabulous sentence'.split()

list(map(count_vowels, words))
print(map(count_vowels, words))
print(*map(count_vowels, words))
import time
time.time()
import numpy as np
# np.nparray is the data structure we want
# but we'll build it with np.array, passing it a list

a = np.array([10, 20, 30, 40, 50, 60])
a
# many standard Python things work with a NumPy array

a[0]
a[1]
a[-1]
s[2:5]
a[2:5]
