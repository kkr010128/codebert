import collections
N = int(input())
ls = list(map(int,input().split()))
count = collections.Counter(ls)
for i in range(1,N+1):
    if i in count.keys():
        print(count[i])
    else:
        print(0)