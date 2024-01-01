# IPython log file


def myfunc(x, y):
    for one_number in range(x, y):
        yield one_number
myfunc(10, 20)
for one_item in myfunc(10, 20):
    print(one_item)
def evenrange(start, finish):
    for one_number in range(start, finish):
        if one_number % 2:
            continue
        yield one_number
for one_item in evenrange(10, 20):
    print(one_item)
def myfunc():
    return f'Hello, world!'
def mygen():
    yield f'Hello, world!'
muyfunc()
myfunc()
mygen()
type(myfunc)
type(mygen)
myfunc.__code__.co_consts
myfunc.__code__.co_flags
hex(myfunc.__code__.co_flags)
bin(myfunc.__code__.co_flags)
bin(mygen.__code__.co_flags)
import dis
dis.show_code(myfunc)
dis.show_code(mygen)
def myfunc():
    return 1
    return 2
    return 3
dis.dis(myfunc)
def myfunc():
    if False:
        yield 'Hello'
    
dis.show_code(myfunc)
g1 = evenrange(10, 20)
g2 = evenrange(10, 20)
g3 = evenrange(10, 20)
next(g1)
next(g1)

next(g1)
g1.gi_frame.f_lineno
g2.gi_frame.f_lineno
def read_n(filename, n):
    with open(filename) as f:
        while True:
            output = f.readline()
    
            if output:
                yield output
            else:
                return

for one_chunk in read_n('/etc/passwd', 5):
    print(one_chunk)
# let's take n into account

def read_n(filename, n):
    with open(filename) as f:
        while True:
            output_lines = []
            
            for i in range(n):
                output_lines.append(f.readline())

            output = ''.join(output_lines)
                
            if output:
                yield output
            else:
                return
for one_chunk in read_n('/etc/passwd', 5):
    print(one_chunk)
# let's take n into account

def read_n(filename, n):
    with open(filename) as f:
        while True:
            output = ''.join([f.readline()
                              for i in range(n)])
                
            if output:
                yield output
            else:
                return

for one_chunk in read_n('/etc/passwd', 7):
    print(one_chunk)
# list comprehension

[x*x
 for x in range(-10, 10)]
# set comprehension

{x*x
 for x in range(-10, 10)}
# dict comprehension

{x : x*x
 for x in range(-10, 10)}
#  tuple comprehension?

(x*x
 for x in range(-10, 10))
# generator expression / generator comprehension

(x*x
 for x in range(-10, 10))
# generator expression / generator comprehension

g = (x*x
 for x in range(-10, 10))
g
for one_item in g:
    print(one_item)
mylist = [10, 20, 30]

'*'.join(mylist)   # this won't work -- only can pass a list of strings
# we can use a list comprehension here

'*'.join([str(one_item)
          for one_item in mylist])
# we can also use a generator comprehension

'*'.join((str(one_item)
          for one_item in mylist))
# what about this:
# we can remove the inner parentheses and it works fine!

'*'.join(   str(one_item)
            for one_item in mylist    )
'*'.join(   print(one_item)
            for one_item in mylist    )
(   print(one_item)
    for one_item in mylist    )
g = (   print(one_item)
    for one_item in mylist    )
next(g)
print(next(g))
g = (   print(one_item)
    for one_item in mylist    )
list(g)
numbers = {x*x
 for x in range(-10, 10)}
print(numbers)
numbers
d = {}
d['a'] = 100    
hash('a')
hash('a') % 8
filename = '/etc/passwd' 

[ one_character
  for one_line in open(filename)
  for one_character in one_line ]
filename = '/etc/passwd' 

[ one_character
  for one_line in open(filename)
  for one_character in one_line 
  if one_character in 'aeiou']
filename = '/etc/passwd' 

( one_character
  for one_line in open(filename)
  for one_character in one_line 
  if one_character in 'aeiou')
