def add(a,b):
    return a+b

print(add(2,4))


def myFunction(a,b,*c,**d):
    print('a',a)
    print('b',b)
    print('c',c)
    print('d',d)

myFunction(1,2,3,4,5,name='hero',village='mumbai')