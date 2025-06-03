s = 100000
n = int(input())
for i in range(n):
    s *= 1.05
    if s % 1000 != 0:
        s = s // 1000 * 1000 + 1000
    else:
        pass
print(int(s))
