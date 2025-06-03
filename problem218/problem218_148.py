import collections
n=int(input())
data=[""]*n
for i in range(n):
    data[i]=input()
data=sorted(data)
count=collections.Counter(data)
num=max(count.values())
for v,k in count.items():
    if k==num:
        print(v)