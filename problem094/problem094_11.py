import numpy as np
def main(R,C,K,RCV):
    V=np.zeros((R+1,C+1),dtype=np.int64)
    for i in range(K):
        V[RCV[i][0]][RCV[i][1]]=RCV[i][2]
    d=np.zeros((R+1,C+1,4),dtype=np.int64)
    for i in range(R):
        for j in range(C):
            m=max(d[i][j+1])
            d[i+1][j+1][0]=m
            for k in range(3):
                d[i+1][j+1][k+1]=max(d[i+1][j][k+1],m+V[i+1][j+1],d[i+1][j][k]+V[i+1][j+1])
    return max(d[-1][-1])
import sys
readline=sys.stdin.buffer.readline
read=sys.stdin.buffer.read
if sys.argv[-1]=='ONLINE_JUDGE':
    from numba import*
    from numba.pycc import CC
    cc=CC('my_module')
    def cc_export(f,s):
        cc.export(f.__name__,s)(f)
        return njit(f)
    main=cc_export(main,(i8,i8,i8,i8[:,:],))
    cc.compile()
    exit()
R,C,K=np.array(readline().split(),dtype=np.int64)
RCV=np.array(read().split(),dtype=np.int64).reshape(K,3)
from my_module import main
print(main(R,C,K,RCV))
