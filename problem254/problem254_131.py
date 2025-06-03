a = int(input())
b = int(input())

ans = 0

if a == 1:
    if b == 2:
        ans = 3
    else:
        ans = 2
elif a == 2:
    if b == 1:
        ans = 3
    else:
        ans = 1
else:
    if b == 1:
        ans = 2
    else:
        ans = 1

print(ans)