while 1:
 n,x=map(int,input().split())
 if n+x==0:break
 print(sum([1 for i in range(3,n+1)for j in range(2,x-i)if x-i-j<j<i]))