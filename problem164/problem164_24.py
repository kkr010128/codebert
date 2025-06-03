a, b, c, d = map(int, input().split())

taka = 0
aoki = 0

while a > 0:
    a = a - d
    taka += 1   

while c > 0:
    c = c - b
    aoki += 1

if taka < aoki:
    print("No")
else:
    print("Yes")
