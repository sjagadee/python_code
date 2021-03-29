def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0
     
li = [1,2,3,4,5,6,7,8,9,10 ]

#  filter function is used to reduce the list using the function
b = list(filter(isOdd, li))

print(b)

#  map will retain the same function but would implement the function on each value of the list
c = list(map(add7, b))

print(c)