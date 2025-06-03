n = int(input())
a = list(map(int,input().split()))

from collections import Counter
b = Counter(a)

for i in b.values():
    if i>1:
        print('NO')
        break
else:
    print('YES')