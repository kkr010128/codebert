n = int(input())
*a, = map(int, input().split())
ans = 1000
for i, j in zip(a, a[1:]):
    if i<j:
        ans = ans//i*j + ans%i
print(ans)