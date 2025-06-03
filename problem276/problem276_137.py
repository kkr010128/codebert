N = input()
A = list(map(int, input().split()))
S = sum(A)
m = S
tmp = 0
for a in A:
    tmp += a
    m = min(m, abs(tmp-(S-tmp)))
print(m)
