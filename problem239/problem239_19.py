moji="abcdefghijklmnopqrstuvwxyz"
C=input()
x=[]
for i in range(26):
  x.append(moji[i])
print(x[x.index(C)+1])