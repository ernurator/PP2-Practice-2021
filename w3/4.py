three = [x for x in range(100) if x % 3 == 0]
print(three)

l = [2*x for x in range(10)]
# print(l)
# [value for var in iterable {if bool}]
# x  | 3 5 7 9
# 2x | 6 10 14 18

# foreach: elem is element from list
for elem in l:
    print(elem)

# i is index, l[i] is element of l
for i in range(len(l)):
    print(i, l[i])
