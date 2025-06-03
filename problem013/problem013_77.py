n = int(raw_input())
minv = int(raw_input())
maxv = -1*10**9  

for j in range(n-1):
    a = int(raw_input())
    b = a- minv
    if maxv < b:
       maxv = b 
    if minv > a:
       minv = a

print maxv