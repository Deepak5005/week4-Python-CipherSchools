# Raise errors in python
def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    return 'OOPs you are passing wrong data type to function'

print(add('2','3'))