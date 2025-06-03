A, B, C, K = map(int, input().split())
num = 0

if K - A <= 0:
    num = K
else:
    K -= A
    num = A
    if K - B > 0:
        K -= B
        num += (-1)*K

print(num)