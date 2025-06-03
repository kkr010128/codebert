n = int(input())
title = []
length = []
for i in range(n):
  a,b = map(str, input().split())
  title.append(a)
  length.append(int(b))
x = input()

ind = title.index(x)
print(sum(length[ind+1:]))