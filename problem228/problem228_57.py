H=int(input())
atk=0
m=1
while H>1:
  atk+=m
  m*=2
  H=H//2
atk+=m
print(atk)