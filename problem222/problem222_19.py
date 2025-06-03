from collections import Counter
from sys import exit

N = int(input())
A = list(map(int,input().split()))

cnt = Counter(A)

for i in cnt.values():
    if i != 1:
        print("NO")
        exit(0)

print("YES")