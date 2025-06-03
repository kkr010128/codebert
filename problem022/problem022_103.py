n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]
ans = 0
for t in T:
    if t in S:
        ans += 1

print(ans)

