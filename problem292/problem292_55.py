n=int(input())
l=list(map(int,input().split()))
prod=0
for i in range(n):
    for j in range(i+1,n):
        prod=prod+(l[i]*l[j])
print(prod)
