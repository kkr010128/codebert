from collections import Counter
n=int(input())
a=list(map(int, input().split()))

cnt=Counter(a)

for k in cnt.values():
    if k != 1:
        print('NO')
        break
else:
    print('YES')