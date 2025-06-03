import sys
import math
def Ii():return int(sys.stdin.buffer.readline())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))
 
x = Ii()
ans = 0
k = 100
while x > k:
  tax = k//100
  k += tax  
  ans += 1
  
print(ans)