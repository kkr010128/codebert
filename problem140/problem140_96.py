T = list(input())
tlen = len(T)

for i in range(0, tlen):
  if T[i] == '?':
    T[i] = 'D'
    
print(*T,sep='')