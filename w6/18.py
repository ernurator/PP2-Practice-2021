
x = 10
s = """
x += 10
print(x)
"""

exec(s)
print(eval('x**2 + x'))
