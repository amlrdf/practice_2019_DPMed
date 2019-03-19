from copy import copy, deepcopy
def update_value(c):
    c[0] = 20
    return c

a = [[1, 2, 3]]
b = deepcopy(a)
b[0][1] = 5
print(a)
print(b)

c = [1, 2, 3]
d = copy(c)
d[2] = 10
print(c, d)
c = update_value(c)
print(c)