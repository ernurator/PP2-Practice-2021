# l, r, n = map(int, input().split())

l, r, n = [int(x) for x in input().split()]

# '5 9 6'
# ['5', '9', '6']
# [5, 9, 6]


if l <= n <= r:
    print('In the range')
else:
    print('Not in the range')
