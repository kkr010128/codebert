A, B = list(map(int, input().split()))

if B * 2 < A:
    ans = A - B * 2
else:
    ans = 0
print(ans)