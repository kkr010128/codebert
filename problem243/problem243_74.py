N=int(input())
S=["a"]*N
T=[0]*N

for i in range(N):
  S[i],T[i]=input().split()
X=input()
flag=0
x=0
for i in range(N):
  if flag==1:
    x+=int(T[i])
  elif X==S[i]:
    flag=1
print(x)
