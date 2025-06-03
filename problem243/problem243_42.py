import collections
n = int(input())
s_ls = []
dic = collections.defaultdict(int)
for i in range(n):
    [s,t] = [j for j in input().split()]
    s_ls.append(s)
    dic[s] = int(t)
x = input()
f = 0
ans = 0
for i in range(n):
    if f:
        ans += dic[s_ls[i]]
    if x == s_ls[i]:
        f = 1
print(ans)
