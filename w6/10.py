a = [1, 2, 3, 4, 6, 8, 9]

# b = list(filter(lambda x: x % 2 == 0, a))
b = [x for x in a if x % 2 == 0]
print(b)
