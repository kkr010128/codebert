A, B, K = map(int, input().split())

if A > K:
    after_A = A - K
    after_K = 0
else:
    after_A = 0
    after_K = K - A

if B > after_K:
    after_B = B - after_K
    final_K = 0
else:
    after_B = 0
    final_K = after_K - B

print(after_A, after_B)