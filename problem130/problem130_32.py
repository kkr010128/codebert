import random
s = str(input()).lower()
t = random.randint(0, len(s)-3)
print(s[t:t+3])