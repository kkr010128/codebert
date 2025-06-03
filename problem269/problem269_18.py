T = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


da, db = 0, 0
for i in range(2):
    da += T[i] * A[i]
    db += T[i] * B[i]

if da == db:
    print("infinity")
    exit()

x = (B[0] - A[0]) * T[0]
y = da - db

print(max(0, x // y * 2 + (0 if x % y == 0 else 1)))
