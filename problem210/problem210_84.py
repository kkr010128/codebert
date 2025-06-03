N = int(input())
S = list(input())
Q = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
num = dict()
for i, var in enumerate(alphabet):
  num[var] = i

class Bit():
  def __init__(self, N):
    self.__N = N
    self.__arr = [[0] * 26 for _ in range(1 + N)]
    
  def add_(self, x, a, i):
    while(x < self.__N + 1):
      self.__arr[x][i] += a
      x += x & -x
      
  def sum_(self, x, i):
    res = 0
    while(x > 0):
      res += self.__arr[x][i]
      x -= x & -x
    return res
  
  def sub_sum_(self, x, y, i):
    return self.sum_(y, i) - self.sum_(x, i)

Bit = Bit(N)
for i, var in enumerate(S):
  Bit.add_(i+1, 1, num[var])

for i in range(Q):
  q, l, r = input().split()
  l = int(l)
  if q == "1" and r != S[l-1]:
    temp = S[l-1]
    S[l-1] = r
    Bit.add_(l, -1, num[temp])
    Bit.add_(l, 1, num[r])
  elif q == "2":
    r = int(r)
    res = 0
    for j in range(26):
      res += min(1, Bit.sub_sum_(l-1, r, j))
    print(res)    
    
