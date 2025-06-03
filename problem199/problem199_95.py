S=list(str(input()))
A=''
B=''
while len(S)>0:
    A+=S.pop()
    if len(S)>0:
        B+=S.pop()
if (len(A)+len(B))%2!=0:
    print('No')
elif len(set(A))==len(set(B))==1:
    if 'h' in A or 'i' in A:
        if 'h' in B or 'i' in B:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
