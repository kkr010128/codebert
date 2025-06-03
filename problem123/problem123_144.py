import sys
def Ii():return int(sys.stdin.readline())
def Mi():return map(int,sys.stdin.readline().split())
def Li():return list(map(int,sys.stdin.readline().split()))

n = Ii()
a = Li()
b = 0
for i in range(n):
  b ^= a[i]
ans = []
for i in range(n):
  print(b^a[i],end=' ') 