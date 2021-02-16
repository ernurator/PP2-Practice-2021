# https://informatics.msk.ru/mod/statements/view.php?id=4163&chapterid=3853

l = input().split()
k = int(input())
k %= len(l)
for elem in l[-k:] + l[:-k]:
    print(elem, end=' ')
