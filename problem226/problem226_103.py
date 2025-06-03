H, N = map(int, input().split())
A = map(int, input().split())
A_sum = sum(A)

print("Yes" if H - A_sum <= 0 else "No")