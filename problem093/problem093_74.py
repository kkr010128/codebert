#import sys

#import numpy as np


def main(n,k,p,c):
    ans = -10**9
    for i in range(n):
        x = i
        t = k
        count = 0
        l = True
        sub = 0
        ln = 0
        while True:
            x = p[x] - 1
            if l:
                count += c[x]
                ln += 1
                if x == i:
                    if t > ln:
                        if count > 0:
                            sub += (t // ln - 1) * count
                            t %= ln
                            t += ln
                        else:
                            t = 0
                    l = False
            sub += c[x]
            t -= 1
            ans = max(sub, ans)
            if t < 1:
                break
    return ans


# >>> numba compile >>>
#if sys.argv[-1]=='ONLINE_JUDGE':
#  from numba.pycc import CC
#  cc=CC('my_module')
#  cc.export('main','i8(i8,i8,i8[:],i8[:])')(main)
#  cc.compile()
#  exit()
#from my_module import main
# <<< numba compile <<<
(n, k), p, c = [[*map(int,i.split())] for i in open(0)]
print(main(n,k,p,c))
