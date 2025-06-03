n = int(input())
title = []
length = []
for i in range(n):
    a, b = input().split()
    title.append(a)
    length.append(int(b))
i = title.index(input())
print(sum((length[i+1:])))