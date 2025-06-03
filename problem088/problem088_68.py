N = int(input())
A = [int(i) for i in input().split()]
ans = 0
now = A[0]
for a in A:
    if now > a:
        ans += now -a
    if now < a:
        now = a
print(ans)