def mult(a):
    res = 1
    for elem in a:
        res *= elem
    
    return res

a = [1, 2, 3, 4]
print(mult(a))
