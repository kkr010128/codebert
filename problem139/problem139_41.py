import sys
def Ii():return int(sys.stdin.buffer.read())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

h1,m1,h2,m2,k = Mi()
ans = h2*60+m2-h1*60-m1-k
print(ans)