S = int(input())
m = (10**9)+7
lists=[1]+[0]*(S)

for i in range(S):
  for j in range(3,S+1):
    try:
      lists[i+j]+=lists[i]
    except IndexError:
      break
      
print ((lists[S])%m)