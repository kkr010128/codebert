n = int(input())
d = 10**9 + 7

if n == 1:
    print(0)

else:
    ans = 10 ** n - 9 ** n - 9 ** n + 8 ** n
    print(ans % d)