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
