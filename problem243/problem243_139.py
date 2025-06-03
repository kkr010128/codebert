N = int(input())
s = [0] * N
t = [0] * N
for i in range(N):
    s[i], t[i] = map(str, input().split())
for i in range(N):
    t[i] = int(t[i])
X = input()

not_listened = False
ans = 0
for i in range(N):
    if not_listened:
        ans += t[i]
    if s[i] == X:
        not_listened = True
print(ans)
