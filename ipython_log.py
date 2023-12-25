# IPython log file


import gc
gc.get_referrers(MyDescriptor)
class MyDescriptor:
    def __init__(self):
        print(f'In MyDescriptor.__init__')
    def __get__(self, instance, owner):
        print(f'In MyDescriptor.__get__')
        return 12345
    def __del__(self):
        print(f'Now deleting instance of MyDescriptor')

class MyClass:
    x = MyDescriptor()   # x is a class attribute, its value is instance of MyDescriptor

m = MyClass()
print(m.x)
print(m.x * 2)
gc.get_referrers(MyDescriptor)
del(m)
del(MyClass)
del(MyDescriptor)
import gc
gc.get_referrers(MyDescriptor)
# context manager

class MyCM:
    def __init__(self, x):
        print(f'In MyCM.__init__, {x=}')
        self.x = x

    def __enter__(self, an_instance):
        print(f'In MyCM.__enter__')
        return self

    def __exit__(self, *args):
        print(f'In MyCM.__exit__, {args=}')
        return True

m = MyCM(10)
print(m.x)




    
with MyCM(10) as m:
    print('Inside')
# context manager

class MyCM:
    def __init__(self, x):
        print(f'In MyCM.__init__, {x=}')
        self.x = x

    def __enter__(self):
        print(f'In MyCM.__enter__')
        return self

    def __exit__(self, *args):
        print(f'In MyCM.__exit__, {args=}')
        return True

m = MyCM(10)
print(m.x)




    
with MyCM(10) as m:
    print('Inside')
s = 'abcd'

for one_character in s:
    print(one_character)
iter(s)
iter([10, 20, 30])
iter(5)
i = iter(s)

next(i)
next(i)
next(i)
next(i)
next(i)
