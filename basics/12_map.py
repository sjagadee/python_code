# map function
 
li = [1,2,3,4,5,6,7,8,9,10 ]

def func(x):
    return x ** x

newList = []

for x in li:
    newList.append(func(x))

print(newList)

#  ******** above way is a valid way to do it, but using map

print(list(map(func, li)))

#  list comprihension 

print([func(x) for x in li if x%2==0])