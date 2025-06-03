A,B,C,K = map(int,input().split())

point = 0 

if K-A >=0:
    point += A
else:
    point += K
if K-A-B > 0:
    point -= K-A-B
print(point)