N = int(input())
C = input()

r_n = 0
ans = 0
for c in C:
    if c == 'R':
        r_n += 1

for i in range(r_n):
    if C[i] == 'W':
        ans += 1

print(ans)