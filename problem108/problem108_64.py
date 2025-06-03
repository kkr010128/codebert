n = int(input())
div = n // 1000
if (n % 1000 == 0):
    ans = 0
else:
    ans = (div + 1) * 1000 - n

print(ans)
