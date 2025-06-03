N=int(input())
S=input()

count=0
for i in range(N):
  if S[i]=='A' and i!=N-1:
    if S[i+1]=='B' and i!=N-2:
      if S[i+2]=='C':
        count+=1
print(count)