k = int(input())
a, b = list(map(int, input().split()))

ans = 'NG'

for i in range(1000 // k + 1):
    if a <= i * k <= b:
        ans = 'OK'
        break

print(ans)
