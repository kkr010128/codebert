n = int(raw_input())
S = map(int, raw_input().split())

q = int(raw_input())
T = map(int, raw_input().split())

ans = 0

for i in T:
    if i in S:
        ans += 1

print ans