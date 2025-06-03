N=int(input())
#people
li = list(map(int, input().split()))
Ave1=sum(li)//N
Ave2=sum(li)//N+1
S1=0
S2=0
for i in range(N):
  S1=S1+(Ave1-li[i])**2
for i in range(N):
  S2=S2+(Ave2-li[i])**2

if S1>S2:
  print(S2)
else:
  print(S1)