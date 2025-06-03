
n = int(input())

m = 10**9+7

a = 10 ** n

b = 9 ** n

c = 9 ** n

d = 8 ** n

ans = (a-(b+c-d)) % m

print(ans)