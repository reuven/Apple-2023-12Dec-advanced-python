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
class MyIterator:
    def __init__(self, data):
        print(f'\tIn __init__, {data=}')
        self.data = data
        self.index = 0

    def __iter__(self):
        print(f'\tIn __iter__, {vars(self)=}')
        return self

    def __next__(self):
        print(f'\tIn __next__, {vars(self)=}')
        if self.index >= len(self.data):
            print(f'\t\tRaising StopIteration')
            raise StopIteration

        value = self.data[self.index]
        self.index += 1
        print(f'\t\tReturning {value=}')
        return value

m = MyIterator('abcd')
for one_item in m:
    print(one_item)
        
len(m)
class Circle:
    def __init__(self, data, maxtimes):
        self.data = data
        self.maxtimes = maxtimes
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.maxtimes:
            raise StopIteration

        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value

c = Circle('abcd', 9)
for one_item in c:
    print(one_item)   
