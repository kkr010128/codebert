C =input()
L =[]
for i in range(97, 123):
    L.append(chr(i)) 
print(L[ord(C)-96])
