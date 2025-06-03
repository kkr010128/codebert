# coding: utf-8
# Your code here!
n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=a[k-1]
for i in range(n-k):
    if a[i]<a[i+k]:
        print('Yes')
    else:
        print('No')
