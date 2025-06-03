n = input().split()
x = int(n[0])
y = int(n[1])
if x < y:
    bf = x
    x = y
    y = bf
while y > 0:
    r = x % y
    x = y
    y = r

print(str(x))