N, D = map(int, input().split())
count = 0
for i in range(N):
    a, b = map(int, input().split())
    if (a*a + b*b) <= D*D:
        count += 1
print(count)
