import math
A,B = map(int, input().split())

# 最大公約数の算出
y = max(A,B)
x = min(A,B)
while y%x != 0:
  tmp = x
  x = y%x
  y = tmp

# 素因数分解
p = []
tmp = int(math.sqrt(x))+1
for n in range(2,tmp):
  while x % n == 0:
    x /= n
    p.append(n)
p.append(int(x))
p.append(1)
p = list(set(p))
print(len(p))
  
  
