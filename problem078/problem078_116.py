prime = 10 ** 9 + 7
n = int(input())
ans = 10 ** n - (9 ** n) * 2 + 8 ** n
ans %= prime
print(ans)