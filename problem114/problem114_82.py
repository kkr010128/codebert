D=int(input())
c=[None]+list(map(int, input().split()))
s=[None]+[list(map(int, input().split())) for _ in range(D)]
T=[None]+[int(input()) for _ in range(D)]

lastdi=[None]+[0]*26

v=0

for i in range(1, D+1):
  v+=s[i][T[i]-1]
  lastdi[T[i]]=i
  for x in range(1, 27):
    v-=(i-lastdi[x])*c[x]
    
  print(v)