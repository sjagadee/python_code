def add4(x):
    return x+4

func = lambda x: x+8

func2 = lambda x, y, z=3: x+y*z

print(func2(2, 3))

print(func(5))

print(add4(3))

li = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x:x*2, li))

print(newList)