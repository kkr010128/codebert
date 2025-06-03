s,t=list(input().split())
a,b=list(map(int,input().split()))
u=input()
 
if u==s:
  print(str(a-1)+" "+str(b))
else:
  print(str(a)+" "+str(b-1))