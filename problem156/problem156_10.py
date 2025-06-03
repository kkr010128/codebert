import sys
def Ii():return int(sys.stdin.buffer.read())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

x = Ii()

for i in range(121):
  for j in range(-119,120):
    if x == i**5 - j**5:
      print(i,j)
      exit(0)