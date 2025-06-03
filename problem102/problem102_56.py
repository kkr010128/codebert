from sys import stdin,stdout
n,k=map(int,stdin.readline().split())
a=list(map(int,stdin.readline().split()))
for i in range(k,n):
    print('Yes' if a[i]>a[i-k] else 'No')