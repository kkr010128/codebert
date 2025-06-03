n = int(input())
S = set(map(int, input().split()))
q = int(input())
T = set(map(int, input().split()))

ans = 0
for t in T:
    ans += 1 if t in S else 0
print(ans)

