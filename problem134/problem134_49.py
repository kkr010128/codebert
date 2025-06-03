input()
a=1
d=1000000000000000000
for i in input().split():
  a*=[int(i),1][(a>d)*(i!='0')]
print([a,-1][a>d])