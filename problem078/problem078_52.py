n = int(input())

all_result = 10 ** n
nothing = 8 ** n
only_1 = 9 ** n

result = all_result + nothing - 2 * only_1

print(result % (10**9+7))