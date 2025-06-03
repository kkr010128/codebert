from collections import Counter
n = int(input())
a = list(map(int,input().split()))
q = int(input())
num = Counter(a)
s = sum(a)
for _ in range(q):
    b,c = map(int,input().split())
    s += (c-b)*num[b]
    num[c] += num[b]
    num[b] = 0
    print(s)