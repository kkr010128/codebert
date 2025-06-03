n=int(input())
a=list(map(int,input().split()))
b=[i&1 for i in a[::2]]
print(sum(b))