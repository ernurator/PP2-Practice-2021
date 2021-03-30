import re

n = int(input())
pattern = re.compile(r'([^ ]+ *)(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=[^a-zA-Z0-9])')
colors = []
for i in range(n):
    s = input()
    colors.extend(re.findall(pattern, s))

for color in colors:
    print(color[1])
