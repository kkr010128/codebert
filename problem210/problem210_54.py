class BIT:
  from operator import add, sub, mul, floordiv
  X_unit = 0
  X_f = add
  X_f_rev = sub

  def __init__(self, seq):
    N = len(seq)
    self.N = N
    self.X = seq[:]
    for i in range(self.N):
      j = i + ((i+1) & -(i+1))
      if j < self.N:
        self.X[j] = self.X_f(self.X[i], self.X[j])
  
  def set_val(self, i, x):
    while(i < self.N):
      self.X[i] = self.X_f(self.X[i], x)
      i += (i+1) & -(i+1)

  def cum_val(self, i):
    res = self.X_unit
    while(i > -1):
      res = self.X_f(res, self.X[i])
      i -= (i+1) & -(i+1)
    return res
  
  #区間[L, R)
  def fold(self, L, R):
    return self.X_f_rev(self.cum_val(R-1), self.cum_val(L-1))
  
  def bisect_left(self, w):
    if w > self.cum_val(self.N - 1):
      return self.N
    elif self.N == 2:
      return 1
    n = 2**((self.N - 1).bit_length() - 1)
    res = 0
    while(n):
      if res + n - 1 > self.N - 1:
        n //= 2
        continue
      if w <= self.X[res + n - 1]:
        n //= 2
      else:
        w -= self.X[res + n - 1]
        res += n
        n //= 2
    return res
  
  def bisect_right(self, w):
    if w >= self.cum_val(self.N - 1):
      return self.N
    elif self.N == 2:
      return 1
    n = 2**((self.N - 1).bit_length() - 1)
    res = 0
    while(n):
      if res + n - 1 > self.N - 1:
        n //= 2
        continue
      if w < self.X[res + n - 1]:
        n //= 2
      else:
        w -= self.X[res + n - 1]
        res += n
        n //= 2
    return res
  
  def lower_bound(self, w):
    ans = self.bisect_right(self.cum_val(w))
    if ans == self.N:
      return -1
    else:
      return ans
  
  def upper_bound(self, w):
    ans = self.bisect_left(self.cum_val(w-1))
    return ans

N = int(input())
S = list(input())

L = [BIT([0]*N) for _ in range(26)]

for i in range(N):
  L[ord(S[i])-97].set_val(i, 1)

Q = int(input())

for _ in range(Q):
  q, a, b = input().split()
  if q == "1":
    a = int(a)
    L[ord(S[a-1])-97].set_val(a-1, -1)
    L[ord(b)-97].set_val(a-1, 1)
    S[a-1] = b
  else:
    a, b = int(a), int(b)
    ans = 0
    for i in range(26):
      if L[i].fold(a-1, b) >= 1:
        ans += 1
    print(ans)