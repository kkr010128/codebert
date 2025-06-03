N = int(input())
C = input()
a = 0
rr = 0
lw = 0

for i in range(N):
    if C[i] == 'R':
        rr += 1
a = rr
for i in range(0, N):
    if C[i] == 'W':
        lw = lw+1
    else:
        rr = rr-1
    a = min(a, max(lw, rr))

print(a)
