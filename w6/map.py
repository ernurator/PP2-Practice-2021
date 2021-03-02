a = ['hello', 'pp2', '12345', 'd']

# def my_map(a, f):
#     b = []
#     for elem in a:
#         b.append(f(elem))
#     return b

b = list(map(len, a))

for elem in b:
    print(elem, end=' ')

print()

for elem in b:
    print(elem, end=' ')
