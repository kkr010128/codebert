while 1:
 n=int(input())
 if n==0:break
 s=list(map(int,input().split()))
 print((sum([(m-sum(s)/n)**2 for m in s])/n)**.5)