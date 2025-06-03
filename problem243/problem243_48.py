N = int(input())
s = []
t = []
for i in range(N) :
    p, q = input().split()
    s.append(p)
    t.append(int(q))
X = input()

xi = s.index(X)
ans = 0
for i in range(xi+1, N) :
    ans += t[i]

print(ans)
