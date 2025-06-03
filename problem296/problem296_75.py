s = input()
k = int(input())
n = len(s)
ss = set(s)
# print(ss)
ans = 0
if len(ss) == 1:
    print(k*n//2)
    # print('y')
    exit()
if n == 1:
    print(n//2)
    exit()
streaks = []
cnt = 0
now = s[0]
for i in range(n):
    if now == s[i]:
        cnt += 1
    else:
        streaks.append(cnt)
        now = s[i]
        cnt = 1
streaks.append(cnt)
# print(streaks)
m = len(streaks)
if s[0] == s[-1]:
    for i in range(1, m-1):
        ans += streaks[i]//2
    # print(ans)
    ans *= k
    # print(ans)
    ans += (streaks[0] + streaks[m-1])//2*(k-1)
    # print(ans)
    ans += streaks[0]//2 + streaks[m-1]//2
    # print(ans)
else:
    for i in range(m):
        ans += streaks[i]//2
    ans *= k

print(ans)
