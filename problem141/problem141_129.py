n = int(input())
a = list(map(int, input().split()))
if n == 0 and a[0] == 0:
    print(-1)
    exit()
if n != 0 and a[0] >= 1:
    print(-1)
    exit()
if n == 0 and a[0] >= 2:
    print(-1)
    exit()
ar = list(reversed(a))
#print(ar)
com = [ar[0]]
for i in range(n):
    com.append(com[i] + ar[i+1])
#print(com)
com.reverse()
ans = 1
val = 1
for i in range(1,n+1):
    val *= 2
    ans += min(val,com[i])
    val -= a[i]
    if (i < n and val <= 0) or (i == n and val < 0):
        print(-1)
        exit()
print(ans)
