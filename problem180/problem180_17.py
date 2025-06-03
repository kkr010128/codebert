n, k = map(int, input().split())
if n>k:
  n= n-(n//k)*k
while n >abs(k-n):
  n= abs(k-n)
print(n)