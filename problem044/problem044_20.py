a,b,c = map(int, raw_input().split())

ans = 0
for i in range(c):
    num = c % (i + 1)
    if num == 0:
        if a <= i + 1 and i + 1 <= b:
            ans += 1

print ans