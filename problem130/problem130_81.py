import random
S = input()

A = random.randint(0, len(S) - 3)

print(S[A] + S[A + 1] + S[A + 2])
