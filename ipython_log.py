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
for one_item in a:
    print(one_item)
# some other ways to create NumPy arrays

a = np.random.randint(0, 100, 10)    # 10 ints from 0-100
a
a = np.random.rand(10)   # 10 floats from 0-1
a
a = np.arange(20)
a
# fancy indexing -- I can request multiple indexes

np.random.seed(0)   
a = np.random.randint(0, 100, 10)
a
a[  [3, 5, 2]  ]
# methods on our NumPy array

a.sum()
a.min()
a.max()
a.mean()
a.std()
a.size
a
# what happens when I add a to itself?
a + a
a1 = np.array([10, 20, 30, 40, 50])
a2 = np.array([100, 200, 300, 400, 500])
a3 = np.array([25, 50, 75])

a1 + a3
a1 / a2
# broadcast

a
a + a
a + 3 
a ** 3
np.__add__
a.__add__(3)
a.__pow__(3)
min_temps = np.array([13, 12, 12, 11, 11, 11, 10, 12, 10, 8])
max_temps = np.array([19, 20, 18, 22, 24, 22, 19, 18, 16, 15])
max_temps.mean()
max_temps[:3]
max_temps[:3].mean()
max_temps[range(3)].mean()
# fancy indexing
max_temps[range(3)].mean()
max_temps[[0, 1, 2]].mean()
max_temps - min_temps
(max_temps - min_temps).mean()
max_temps - min_temps.mean()
(max_temps - min_temps).mean()
min_temps * (9/5) + 32
max_temps * (9/5) + 32
(max_temps * (9/5) + 32) - (min_temps * (9/5) + 32) 
((max_temps * (9/5) + 32) - (min_temps * (9/5) + 32)).mean()
((max_temps * (9/5) + 32) - 
 (min_temps * (9/5) + 32)).mean()
a
a = np.array([10, 20, 30, 40, 50])
a
a[[2, 4]]
# what happens if I do this?
a[ [True, False, False, True, True] ]
# broadcast with comparison operators

a < 30
a == 30
# I can use this comparison + mask indexes to filter

a[a < 30]
# I can use this comparison + mask indexes to filter

# 1. First, we execute a<30, and we get back a boolean array
# 2. Then we use the resulting boolean array as a mask/boolean index on a
# 3. We get back a new array, based on a, where the condition was True

a[a < 30]
# I want to see all min temperatures less than 20 degrees

min_temps < 20
# I want to see all min temperatures less than 15 degrees

min_temps < 15
# I want to see all min temperatures less than 12 degrees

min_temps < 12
# I want to see all min temperatures less than 12 degrees

min_temps[min_temps < 12]
# find the max temp on days when the min temp is < 12

max_temps[min_temps < 12]
# what if I want two conditions together, using "and" or "or"?

# for example: I want all of the minimum temps that are (a) < 12 and (b) odd

min_temps[min_temps < 12 and min_temps % 2 == 1]
# what if I want two conditions together, using "and" or "or"?

# for example: I want all of the minimum temps that are (a) < 12 and (b) odd

min_temps[min_temps < 12 & min_temps % 2 == 1]
# what if I want two conditions together, using "and" or "or"?

# for example: I want all of the minimum temps that are (a) < 12 and (b) odd

min_temps[(min_temps < 12) & 
          (min_temps % 2 == 1)]
# what if I want two conditions together, using "and" or "or"?

# for example: I want all of the minimum temps that are (a) < 12 and (b) odd

# "and" in NumPy is &
# "or" in NumPy is |
# "not" in NumPy is ~

min_temps[(min_temps < 12) & 
          (min_temps % 2 == 1)]
min_temps < 12
(min_temps < 12) * 5
min_temps[(min_temps < 12) * 
          (min_temps % 2 == 1)]
False * False
(min_temps < 12) *      (min_temps % 2 == 1)
(min_temps < 12) + (min_temps % 2 == 1)
min_temps
