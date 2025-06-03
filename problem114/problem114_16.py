D=int(input())
c=list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(D)]
t= [int(input()) for i in range(D)]
v=0
LD=[0]*26

for i in range(D):
  v+=s[i][t[i]-1]
  LD[t[i]-1]=i+1  
  for j in range(26):
    v-=c[j]*(i+1-LD[j])
  print(v)