import numpy as np
T=[]
T=list(input())
values = np.array(T)
searchval = '?'
ii = np.where(values == searchval)[0]

if len(ii)>0:
    for k in ii:
        if k==0:
            if len(T)>1:
                if T[k+1]=='D':
                    T[k]='P'
                else:
                    T[k]='D'
            else:
                T[k] = 'D'

        else:
            if T[k-1] == 'P':
                T[k] = 'D'
            else:
                if k+1<len(T):
                    if T[k+1] == 'D':
                        T[k] = 'P'
                    else:
                        T[k]='D'
                else:
                    T[k] = 'D'

newT=''.join(map(str,T))
print(newT)