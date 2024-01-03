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
