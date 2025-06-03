H = int(input())
en = 1
at = 0

while H > 0:
  H //= 2
  at += en
  en *= 2
  
print(at)