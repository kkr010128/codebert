H, N = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
print("Yes") if H - sum(A) <= 0 else print("No")