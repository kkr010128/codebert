from string import ascii_lowercase as LOW
from string import ascii_uppercase as UP

a = {l:u for l,u in zip(list(LOW),list(UP))}
b = {u:l for u,l in zip(list(UP),list(LOW))}
a.update(b)

data = input()
data = [a[s] if s in a else s for s in data]
data = ''.join(data)
print(data)