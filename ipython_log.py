# IPython log file


def myfunc(x, y):
    for one_number in range(x, y):
        yield one_number
myfunc(10, 20)
for one_item in myfunc(10, 20):
    print(one_item)
