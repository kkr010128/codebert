N = int(input())
Alist = list(map(int, input().split()))

Aset = set(Alist)

if len(Aset) == len(Alist):
    print("YES")
else:
    print("NO")
