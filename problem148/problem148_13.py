import sys
readline = sys.stdin.buffer.readline
a,b,c,k =list(map(int,readline().rstrip().split()))
if k <= a:
  print(k)
elif k > a and k <= a + b:
  print(a)
else:
  print(a -(k-(a+b)))
