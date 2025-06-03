n = map(int, input().split())
a = list(map(int, input().split()))

arr = [(x, i + 1) for i, x in enumerate(a)]
arr.sort()

ans = [x[1] for x in arr]

print(*ans)