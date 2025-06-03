n = input()
s = input().split()
q = input()
t = input().split()

ans = 0
for c1 in t:
    for c2 in s:
        if c1 == c2:
            ans += 1
            break

print(ans)