S=[i for i in input()]
T=[j for j in input()]

count=0
for a,b in zip(S,T):
  if a!=b:
    count+=1
print(count)