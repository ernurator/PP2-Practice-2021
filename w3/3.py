# list (mutable, dynamic), tuple (immutable)

t = (12, '34', 10, 36)
# t[0] = 1 - ERROR
# print(t)

# rgb
# 0-255 0-255 0-255
WHITE = (255, 255, 255)

l = [12, 34]
l[0] = 10
l.append('pp2')

l2 = ['asd', 'qwe']
l += l2 # l.extend(l2)

l.append(10)
l.remove(10)
print(l)

