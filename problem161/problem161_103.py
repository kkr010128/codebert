from sys import stdin
input = stdin.readline
 
a,b,n = map(int,input().split())
maxpoint = 0
 
if b > n  :
    tmp = int((a * n) / b)  - a * int(n/b) 
    maxpoint = max(tmp,maxpoint)
else:
    k = int(n/b)*b -1
    maxpoint =  int((a * k) / b)  - a * int(k/b) 
    if b == 1:
        maxpoint = 0
 
print(maxpoint)