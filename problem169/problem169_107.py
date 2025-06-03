import collections

n = int(input())
a  = list(map(int,input().split()))
b = collections.Counter(a)
for d in range(n):
    print(b[d+1])