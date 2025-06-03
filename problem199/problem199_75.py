S=input()
if len(S)%2==1: print('No'); exit()
for i in range(len(S)//2):
    if S[(i*2)]+S[(i*2)+1]!='hi':print('No'); exit()
print('Yes')