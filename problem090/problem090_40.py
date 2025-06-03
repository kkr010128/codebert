S=input()

days=[]
day=0
for i in range(3):
  if S[i]=='R':
    day+=1
  else:
    day=0
  days.append(day)

print(max(days))