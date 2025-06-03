n = int(input())
ns = list(map(int, input().split()))

# min, max, sum は関数名なので
# 別名を使うとよい
min0 = 10000000
max0 = -10000000
sum0 = 0
for x in ns:
  min0 = min(min0, x)
  max0 = max(max0, x)
  sum0 += x
 
print(min0, max0, sum0)
