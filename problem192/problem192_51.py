from collections import Counter

n = int(input())
a = list(map(int,input().split()))

c = Counter(a)
total = sum([v*(v-1)//2 for v in c.values()])
for i in a:
    print(total-(c[i]-1))
