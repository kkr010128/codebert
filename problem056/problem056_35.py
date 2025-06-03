n, m = map(int, raw_input().split())
ans = []
aa = []
for i in range(n):
    a = map(int, raw_input().split())
    aa.append(a)
    ans.append(0)
b = []
for i in range(m):
    a = input()
    b.append(a)
for i in range(n):
    for j in range(m):
        ans[i] += aa[i][j] * b[j]
for i in range(len(ans)):
    print(ans[i])