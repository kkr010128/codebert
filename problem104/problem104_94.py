l, r, d = map(int, input().split())
num = 0
for i in range(r - l +1):
    if (i + l) / d == int((i + l) / d):
        num += 1
print(num)
