N ,K = map(int, input().split()) 

lst = [i for i in range(N+1)]
rlst = [i for i in range(N,-1,-1)]

P = 10**9 + 7
rlt = 0

mini = sum(lst[:K-1])
maxi = sum(rlst[:K-1])

for i in range(N -K + 2):
  mini += lst[K+i-1]
  maxi += rlst[K+i-1]
  rlt += maxi -mini + 1
  rlt %= P
  
print(rlt)