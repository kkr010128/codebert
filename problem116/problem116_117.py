S = input()
T = input()

same = 0

for i in range(len(S)):
  if S[i] == T[i]:
    same += 1
    
print(len(S) - same)