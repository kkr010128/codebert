from collections import deque
import math
import sys

x,y,a,b,c = list(map(int,sys.stdin.readline().split()))
p = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)
q = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)
r = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)
eat=[]

if x<len(p):
    [eat.append(red) for red in p[:x]]
else:
    [eat.append(red) for red in p]
if y<len(q):
    [eat.append(green) for green in q[:y]]
else:
    [eat.append(green) for green in q]
[eat.append(apple) for apple in r]
eat = sorted(eat, reverse=True)
#print(sum(eat[:x + y]))
ans = 0
for taste in eat[:x + y]:
    ans += taste 
print(ans)
