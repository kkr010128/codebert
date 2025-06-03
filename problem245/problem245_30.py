N=int(input())
S=input()
count=0
for i in range(N):
  if S[i]=='A':
    if S[i+1:i+3]=='BC':
      count+=1
print(count)
