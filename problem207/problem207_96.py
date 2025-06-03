a = [0]*9
a[0],a[1],a[2] = map(int,input().split())
a[3],a[4],a[5] = map(int,input().split())
a[6],a[7],a[8] = map(int,input().split())
n = int(input())
ans = [0]*9
for i in range(n):
    b = int(input())
    for j in range(9):
        if b == a[j]:
            ans[j] = 1
if sum(ans[:3]) == 3 or sum(ans[3:6]) == 3 or sum(ans[6:9]) == 3:
    print('Yes')
elif sum(ans[0::3]) == 3 or sum(ans[1::3]) == 3 or sum(ans[2::3]) == 3:
    print('Yes')
elif sum(ans[0::4]) == 3 or sum(ans[2:7:2]) == 3:
    print('Yes')
else:
    print('No') 