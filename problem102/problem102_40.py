from sys import stdin, stdout 
n,k=map(int,input().split())
a=[int(o) for o in input().split()]
prod=1
for i in range(k,n):
    prev=a[i-k]
    if a[i]>prev: stdout.write("Yes\n")
    else: stdout.write("No\n")
