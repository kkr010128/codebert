S = input()
n = len(S) + 1
A = []
mini = 0

for i in range(n-1):
  if i==0:
    if S[i]=="<":
      A.append([1,0])
    else:
      A.append([0,1])
  else:
    if S[i]=="<" and S[i-1]==">":
      A.append([1,0])
    elif S[i]=="<":
      A[-1][0] += 1
    else:
      A[-1][1] += 1

summ = 0
for x in A:
  ma = max(x)
  mi = min(x)
  summ += (ma+1)*ma//2
  summ += (mi-1)*mi//2
print(summ)