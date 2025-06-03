def main():
  import sys
  from collections import deque
  from operator import itemgetter
  
  b = sys.stdin.buffer
  N,D,A = map(int, b.readline().split())
  m = map(int, b.read().split())
  ans = 0
  Q = deque()
  d = 0
  for x,h in sorted(zip(m,m), key=itemgetter(0)):
    while Q and Q[0][0] < x:
      _,d_ = Q.popleft()
      d += d_
    h = h+d
    if h <= 0: continue
    n = -(-h // A)
    d -= n * A
    ans += n
    Q.append((x+2*D,n * A))

  print(ans)
  
main()