import random
S=input()
r = random.randint(0,len(S)-3)
result =""
result = S[r]+S[r+1]+S[r+2]
print(result)
