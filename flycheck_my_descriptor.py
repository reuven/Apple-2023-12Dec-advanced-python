#!/usr/bin/env python3

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


print('About to delete m')
