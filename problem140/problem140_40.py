T=input()
ans=[]
for i in range(len(T)):
    if T[i]=='P':
        ans.append('P')
    elif T[i]=='D':
        ans.append('D')
    else:
        ans.append('D')

print(''.join(ans))