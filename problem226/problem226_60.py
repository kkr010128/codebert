H, N = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
print('Yes' if H - sum(A) <= 0 else 'No')