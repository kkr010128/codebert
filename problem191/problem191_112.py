l = int(input())

ans = 0
for i in range(l * 10 ** 3):
    s = ((l * 10 ** 3 - i) / 2) ** 2
    ans = max(ans, s * i / (10 ** 9))
print(ans)