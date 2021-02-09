# https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3760#1

n = int(input())
d = {}
for i in range(n):
    word1, word2 = input().split()
    d[word1] = word2
    d[word2] = word1

print(d[input()])
