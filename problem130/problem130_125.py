import random


S = input()
n = len(S)
i = 0+int(random.random()*(n-3))
print(S[i]+S[i+1]+S[i+2])