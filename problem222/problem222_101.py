import sys

n = int(input())
a = [int(x) for x in input().split()]
d = set()
for i in a:
    if i in d:
        print("NO")
        exit()
    d.add(i)
print("YES")