import sys
sys.setrecursionlimit(int(1e9))

class uft:
  def __init__(self, N):
    self.__N = N
    self.__arr = [-1] * (N + 1)
  def fp(self, x):
    if self.__arr[x] < 0:
      return x
    else:
      self.__arr[x] = self.fp(self.__arr[x])
      return self.__arr[x]
  def add(self, x, y):
    px = self.fp(x)
    py = self.fp(y)
    if px > py:
      px, py = py, px
    if px == py:
      return 1
    self.__arr[px] += self.__arr[py]
    self.__arr[py] = px
  def groups(self):
    ret = -1
    for i in self.__arr:
      if i < 0:
        ret += 1
    return ret
  def show_arr(self):
    print(self.__arr)
  
N, M = map(int, input().split()) 
UFT = uft(N)

for i in range(M):
  A, B = map(int, input().split())
  UFT.add(A,B)
print(UFT.groups() -1)
