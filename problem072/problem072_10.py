n = int(input())
total = 0
out = 1
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        total += 1
    else:
        if total >= 3:
            out = 0
        else:
            total = 0
if total >= 3:
    out = 0
if out:
    print("No")
else:
    print("Yes")