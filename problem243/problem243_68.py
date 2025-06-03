N = int(input())
S = []
T = []

for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

ind = S.index(input())
ans = sum(T[ind+1:])
print(ans)
