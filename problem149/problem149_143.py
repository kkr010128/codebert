import sys
from itertools import combinations_with_replacement, product
import numpy as np
def input(): return sys.stdin.readline().rstrip()

def main():
    n, m, x = map(int, input().split())
    data = np.zeros((n,m),int)
    clist = np.zeros(n, int)
    ans=10**10
    for i in range(n):
        ca = list(map(int, input().split()))
        clist[i]=ca[0]
        data[i]=np.array(ca[1:])
    for bit in list(product([0,1],repeat=n)):
        if all(np.dot(np.array(bit), data)>=x):
            ans=min(ans,np.dot(np.array(bit),clist.T))
    
    if ans==10**10:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()