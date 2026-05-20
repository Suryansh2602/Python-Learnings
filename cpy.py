import copy
x = 3
y = copy.copy(x)
x = 4
print(x,y)

a = 12
b  = copy.deepcopy(a)
b = 13
print(a,b)