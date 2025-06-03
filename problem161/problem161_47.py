A, B, N = [int(i) for i in input().split(' ')]

if B > N:
    x = N
else:
    x = B - 1

m = int(A * x / B) - A * int(x / B)

print(m)