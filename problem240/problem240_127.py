N, M = map(int, input().split())
L = [list(input().split()) for _ in range(M)]
D_1 = {str(c):False for c in range(1, N+1)}
D_2 = {str(c):0 for c in range(1, N+1)}
for l in L:
  if l[1]=="WA" and D_1[l[0]]==False:
      D_2[l[0]] += 1 
  else:
    D_1[l[0]]=True
S_1 = sum(D_2[k] for k, v in D_1.items() if v)  
S_2 = sum(D_1.values())
print(S_2, S_1)