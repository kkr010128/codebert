N = int(input())
A_lis = list(map(int,input().split()))
ls = [0] * N

for i in range(N-1):
  ls[A_lis[i]-1] += 1
  
for a in ls:
  print(a)