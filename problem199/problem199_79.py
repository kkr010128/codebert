s=input()
if len(s)&1:
    print('No')
    exit()
for i in list(s[i*2:i*2+2] for i in range(len(s)//2)):
    if i!='hi':
        print('No')
        exit()
print('Yes')