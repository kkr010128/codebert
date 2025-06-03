N = int(input())
table = []
for i in range(N):
    X,L = map(int,input().split())
    table.append((X-L,X+L))
table = sorted(table, key=lambda x:x[1])

cur = 0
l_cur, r_cur = table[0]
ans = N
for i in range(1,N):
    l,r = table[i]
    if r_cur > l:
        ans -= 1
    else:
        l_cur, r_cur = l,r
print(ans)