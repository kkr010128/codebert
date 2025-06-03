n = int(input())
nAll = 10**n
nOne = 2*(9**n)
nBoth = 8**n
print((nAll - nOne + nBoth)%(10**9+7))