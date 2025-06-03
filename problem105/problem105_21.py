N = int(input())
a = list(map(int, input().split()))

ans = sum(1 for i, j in enumerate(a) if (i + 1) % 2 == 1 and j % 2 == 1)

print(ans)
