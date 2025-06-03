H, N = map(int, input().split())
A = list(map(int, input().split()))
A = sum(A)
if H > A:
    ans = "No"
else:
    ans = "Yes"
print(ans)
