n = int(input())
c = 0
m = 0
for x in range(n):
    a, b = input().split()
    if a==b:
        c += 1
    else:
        c = 0
    m = max(m, c)
if m >= 3:
    print("Yes")
else:
    print("No")