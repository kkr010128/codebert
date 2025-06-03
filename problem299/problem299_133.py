n = int(input())
A = list(map(int, input().split()))

B = [(a, i + 1) for i, a in enumerate(A)]
B.sort()

ans = [j for _, j in B]

print(*ans)