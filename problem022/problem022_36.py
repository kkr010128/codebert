
n = int(input())
s = [int(i) for i in input().split()]
q = int(input())
t = [int(i) for i in input().split()]

ans = 0
for si in set(s):
    if si in t:
        ans += 1

print(ans)

