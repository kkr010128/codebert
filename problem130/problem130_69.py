
import random

s = input()
start = random.randint(0,len(s)-3)

nickname = s[start:start+3]
print(nickname)
