S =input()
if len(S) % 2 != 0:
    print('No')
    exit()
for i in range(0,len(S),2):
    if S[i:i+2] != 'hi':
        print('No')
        exit()
print('Yes')