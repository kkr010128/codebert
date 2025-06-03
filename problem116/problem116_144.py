S = str(input())
T = str(input())
count=0

for i in range(len(S)):
  if(S[i]==T[i]):
    continue
  else:
    count += 1
print(count)