n = int(input())
a = list(map(int, input().split()))

x = 0
for ai in a:
    x ^= ai

for ai in a:
    print(x ^ ai, end=' ')