S = input()
ans = 'Yes'
if len(S)%2 != 0:
    print('No')
    exit()
for i in range(0,len(S),2):
    if S[i] != 'h':
        print('No')
        exit()
    if S[i+1] != 'i':
        print('No')
        exit()
print('Yes') 
