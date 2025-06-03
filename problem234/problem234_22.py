N = int(input())
D = {i: [0] for i in range(100)}
for i in range(1, N+1):
  if i % 10 != 0:
    s = str(i)
    D[int(s[0])*10+int(s[-1])][0] += 1
    D[int(s[0])*10+int(s[-1])].append(i)
S = 0
for i in range(10):
  for j in range(10):
    S += D[i*10+j][0] * D[j*10+i][0]
print(S)