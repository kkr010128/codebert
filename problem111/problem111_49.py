import math

n = int(input())
a = list(map(int,input().split()))

s = sorted(a,reverse=True)

max = s[0]
for i in range(3,n+1):
  max += s[math.ceil(i/2)-1]
print(max)