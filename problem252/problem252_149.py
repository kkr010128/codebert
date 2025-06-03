import sys
input = sys.stdin.buffer.readline
import numpy as np

def main():
    N,M = map(int,input().split())
    a = np.array(input().split(),np.int64)
    a = np.sort(a)
    cum = np.zeros(N+1,dtype=int)
    cum[1:] = np.cumsum(a)
    
    l,r = -1,10**6+1
    while r-l > 1:
        mid = (l+r)//2
        ab_mid = (N-np.searchsorted(a,mid-a,side="left")).sum()
        if ab_mid >= M:
            l = mid
        else:
            r = mid

    pos_rev = np.searchsorted(a,r-a,side="left")
    count = (N-pos_rev).sum()
    ans = (cum[-1]-cum[pos_rev]).sum()
    ans += (a*(N-pos_rev)).sum()
    ans += (M-count)*l
        
    print(ans)

if __name__ == "__main__":
    main()
