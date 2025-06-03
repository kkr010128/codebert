n=int(input())
a= list(map(int, input().split()))
kt=1
a.sort()
for i in range (0,n-1):
    if a[i]==a[i+1]:
        kt=0
        break
if kt==1:
    print("YES")
else:
    print("NO")