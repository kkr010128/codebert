K = int(input())
 
x = 7
for i in range(K):
  if x % K == 0:
    print(i+1)
    exit()
  else:
    x = (10*x + 7) % K
print(-1)