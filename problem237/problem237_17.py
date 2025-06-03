from operator import itemgetter
n = int(input())
s = []
for i in range(n):
    l = list(map(int, input().split()))
    rang = [l[0] - l[1], l[0] + l[1]]
    s.append(rang)
s_sort = sorted(s, key=itemgetter(1))
ans = 0
last = -float("inf")
for i in range(n):
    if last <= s_sort[i][0]:
        ans += 1
        last = s_sort[i][1]
print(ans)
