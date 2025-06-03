N = int(input())
S = input()

r = S.count('R')
ans = r - S[:r].count('R')
print(ans)