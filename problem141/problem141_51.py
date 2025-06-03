n = int(input())
a = list(map(int,input().split()))

s = 1
if n == 0:
    if a[0] != 1:
        print(-1)
        quit()
    else:
        print(1)
        quit()
elif a[0] > 0:
    print(-1)
    quit()
memo = [[0,0] for _ in range(n+1)]
memo[0] = [0,1]
for i in range(1,n+1):
    if s == 0:
        print(-1)
        quit()
    s = memo[i-1][1]*2
    if s > 10**15:
        s = 10**15
    memo[i][0] = a[i]
    memo[i][1] = s-a[i]
    if s-a[i] < 0:
        print(-1)
        quit()
ans = [[a[i],0] for i in range(n+1)]
for i in range(n-1,-1,-1):
    if (ans[i+1][0]+ans[i+1][1]) > memo[i][1]*2:
        print(-1)
        quit()
    else:
        ans[i][1] = min(memo[i][1],ans[i+1][0]+ans[i+1][1])
s = 0
for i in range(n+1):
    s += sum(ans[i])
print(s)
