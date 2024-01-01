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
