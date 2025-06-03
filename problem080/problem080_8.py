n=int(input())
a= [list(map(int, input().split())) for i in range(n)]
a1=float('inf')
a2=-float('inf')
a3=float('inf')
a4=-float('inf')

for i in range(n):
    cnt=a[i][0]+a[i][1]
    cnt1=a[i][0]-a[i][1]
    a1=min(a1,cnt)
    a2=max(a2,cnt)
    a3=min(cnt1,a3)
    a4=max(cnt1,a4)


print(max(a2-a1,a4-a3))