N = int(input())
A = list(map(int, input().split()))

t = 0
for c in A:
    t ^= c

ans = []
for b in A:
    ans.append(t^b)

print(*ans)