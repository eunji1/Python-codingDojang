import copy
a = [[10, 20], [30, 40]]

#b = a
#b = a.copy()
b = copy.deepcopy(a)

b[0][0] = 500

print(a)
print(b)