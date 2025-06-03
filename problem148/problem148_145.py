A, B, C, K = map(int, input().split())

count_A = 0
count_B = 0
count_C = 0
count = 0
if A >= K:
    count_A += K
else:   # A < K
    K -= A
    count_A += A
    if B >= K:
        count_B += K
    else:
        K -= B
        count_B += B
        count_C += K

print(count_A - count_C)
