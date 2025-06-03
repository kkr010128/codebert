S=list(input())
while len(S)>1:
    if S[0] == 'h' and S[1] == 'i':
        S.remove('h')
        S.remove('i')
    else:   
        break

if len(S) == 0:
    print('Yes')
else:
    print('No')




