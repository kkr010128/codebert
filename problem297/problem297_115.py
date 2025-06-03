N = int(input())

L = [i for i in range(N+1)]

odd = []

for j in range(N+1):
  if L[j] % 2 == 0:
    pass
  else:
    odd.append(L[j])
  j+=1

print(len(odd)/(len(L)-1))
