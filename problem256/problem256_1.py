A,B = map(int,input().split())
Flag = True
i = max(A,B)
s = max(A,B)
while Flag == True and i <= A*B:
  if i%A ==0 and i%B == 0:
    Flag = False
  i += s
print(i-s)