import collections
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
c = collections.Counter(a)
l = [0]*n
for i,x in c.items():
    l[i-1] = x
    
for i in l:
    print(i)