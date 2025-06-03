import sys
def Ii():return int(sys.stdin.buffer.readline())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

k = Ii()
a,b = Mi()

for i in range(a,b+1):
  if i%k == 0:
    print('OK')
    exit(0)
    
print('NG')