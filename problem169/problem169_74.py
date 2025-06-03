import collections

N = int(input())
A = list(map(int,input().split()))
a = collections.Counter(A)

for i in range(1,len(A)+2):
    print(a[i])