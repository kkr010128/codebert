H, A = map(int, input().split())
res = H // A
H -= A * res
print(res + 1 if H > 0 else res)