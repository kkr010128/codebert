n=int(input())
x=list(map(int,input().split()))
avex=sum(x)//n
ansl=0
ansr=0
for i in x:
  ansl+=(avex-i)**2
  ansr+=(avex+1-i)**2

  
print(min(ansl,ansr))