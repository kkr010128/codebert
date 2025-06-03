n=int(input())
a=0
if n%2:print(0)
else:
 m=1
 for i in range(30):a+=n//(m*10);m*=5
 print(a)