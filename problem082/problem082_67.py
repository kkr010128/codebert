S =input()
T = input()
n = len(S)-len(T)+1
count = []

for i in range(n):
  c =0
  for p in range(len(T)):
    if S[i+p] != T[p]:
      c += 1
  count.append(c)
  
print(min(count))
  
	

