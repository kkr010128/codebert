S = raw_input().split(" ")
for i in range(0, len(S)):
  S[i] = int(S[i])

primeNum = 0

for i in range(S[0], S[1]+1):
  if(S[2] % i == 0):
    primeNum = primeNum+1

print(primeNum)