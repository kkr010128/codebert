K = int(input())

a = [0] * K
a[0] = 7 % K

for i in range(1, K):
    a[i] = (a[i-1] * 10 + 7) % K

ans = -1
for i in range(K):
    if a[i] == 0:
        ans = i + 1
        break

print(ans)
