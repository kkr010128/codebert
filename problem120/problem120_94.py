import sys
def Ii():return int(sys.stdin.readline())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

n,k = Mi();
p = Li();
p.sort();
print(sum(p[:k]))
