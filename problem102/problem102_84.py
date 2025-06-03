n,k=map(int,input().split())
a=[int(x) for x in input().rstrip().split()]

ruiseki=[a[0]]
for i in range(k,n):
    if a[i-k]<a[i]:
        print("Yes")
    else:
        print("No")
