n = int(input())
s = list(map(int, input().split()))

m = 1000
stock = 0

for i in range(n-1):
  if s[i+1] >= s[i]:
    #buy
    stock = stock + m // s[i]
    m = m - s[i]*(m//s[i])
  else:
    #sell
    m = m + stock*s[i]
    stock = 0

an  = m + stock*s[n-1]
print(an)