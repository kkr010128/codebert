n=int(input())
a=[int(v) for v in input().split()]
check=1
a.sort()
for i in range (0,n-1):
    if a[i]==a[i+1]:
        check=0
        break
if check==0:
    print("NO")
else:
    print("YES")
