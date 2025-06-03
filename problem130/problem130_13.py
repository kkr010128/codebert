import random

S = input()
x = random.randrange(len(S)-2)
print(S[x] + S[x + 1] + S[x + 2])