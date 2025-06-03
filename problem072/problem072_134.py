n = int(input())
x = 0
for i in range(n):
    d1, d2 = map(int, input().split())
    if x != 3:
        if d1 != d2:
            x = 0
        else:
            x += 1
print("Yes" if x == 3 else "No")