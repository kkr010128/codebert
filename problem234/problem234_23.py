n=int(input())
c = [[0]*10 for i in range(10)]
n_len = len(str(n))
for k in range(1,n+1):
  k_str = str(k)
  l,r=int(k_str[0]),int(k_str[-1])
  c[l][r]+=1

cnt = 0
for i in range(10):
  for j in range(10):
    cnt += c[i][j]*c[j][i]
print(cnt)