import random
S = input()
i = len(S)
m = random.randint(0,i-3)
print (S[m] + S[m+1] + S[m+2])