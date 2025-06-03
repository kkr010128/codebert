#C for submisstion
import numpy as np
from itertools import combinations
H, W, K = map(int, input().split())
C=[input() for i in range(H)]
C_list=[list(C[i]) for i in range(H)]
C_cols=['c'+str(i) for i in range(H)]
C_rows=['r'+str(i) for i in range(W)]
C_comb=C_cols + C_rows

Comb=[]
for i in range(1, H+W):
    Comb+=combinations(C_comb,i)
    
result=0
for i in range(len(Comb)):
    C_array=np.array(C_list)
    for j in Comb[i]:
        if j[0]=='c':
            c_r=int(j[1:])
            C_array[c_r,:]='r'
        else:
            c_r=int(j[1:])
            C_array[:,c_r]='r'
    df_bool = (C_array=='#')
    result+= df_bool.sum()==K
    
if (np.array(C_list) =='#').sum() ==K:
    result+=1
    
print(result)