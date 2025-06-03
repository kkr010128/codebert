n, m = list(map(int, input().split()))
s = []
c = []
for _ in range(m):
    s_i, c_i = list(input().split())
    s.append(int(s_i))
    c.append(c_i)
for i in range(10 ** n):
    num = str(i)
    if len(num) == n and all([num[s[j] - 1] == c[j] for j in range(m)]):
        print(num)
        exit()
print(-1)