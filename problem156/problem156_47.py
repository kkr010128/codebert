X = int(input())
N = int(X**(1/5))
ans = [0,0]
for i in range(-2*N-1, 2*N+2):
  for j in range(-2*N-1, 2*N+2):
    if i**5-j**5==X:
      ans = [i, j]
ans = [str(i) for i in ans]
ans = ' '.join(ans)
print(ans)