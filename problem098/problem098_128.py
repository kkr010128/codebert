N = int(input())
s = input()

w = 0
r = s.count('R')
ans = min(N, r)

for i in range(N):
    if s[i] == 'R':
        r -= 1
    else:
        w += 1
    ans = min(ans, max(w, r))

print(ans)