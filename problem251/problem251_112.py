N, K = map(int, input().split())
R, S, P = map(int, input().split())


dic = {'r':P, 's':R, 'p':S}
flag = [0]*N
rlt = 0

T = input()

for i in range(N):
  if i < K or T[i] != T[i-K] or flag[i-K] == 1:
    rlt += dic[T[i]]
  else:
    flag[i] = 1
    
print(rlt)