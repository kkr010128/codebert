n = int(input())
p = 10 ** 9 + 7

all_ptn = 10 ** n
anti_ptn = 2 * (9 ** n) - 8 ** n

print((all_ptn - anti_ptn) % p)