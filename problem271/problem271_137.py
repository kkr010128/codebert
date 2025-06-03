N = int(input())
S = input()
A = []

for s in S:
  a = ord(s)+N
  if a<=90:
    A.append(chr(a))
  else:
    A.append(chr(64+(a-90)))
    
print(*A,sep="")