n = int(input())
a = list(map(int, input().split()))
ch = 0

for i in range(n):
    if a[i] % 2 == 0:
        if a[i] % 3 != 0 and a[i] % 5 != 0:
            ch = 1

if ch == 0:
    ans = 'APPROVED'
else:
    ans = 'DENIED'

print(ans)
