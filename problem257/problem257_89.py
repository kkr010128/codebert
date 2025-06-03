n=int(input())
a=list(map(int,input().split()))
if not 1 in set(a):
    print("-1")
    exit()
b=1
for i in range(n):
    if a[i]==b:
        b+=1
print(n-b+1)