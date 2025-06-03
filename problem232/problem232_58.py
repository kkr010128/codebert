# -*- coding: utf-8 -*-

import io
import sys
import math

def solve(a,b):
    # implement process
    s = str(min(a,b))
    n = max(a,b)
    return s * n

def main():
    # input
    a,b = map(int, input().split())
    
    # process
    ans = str( solve(a,b) )
    
    # output
    print(ans)
    return ans
        
### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
7 7
"""
_EXPECTED = """\
7777777
"""

def logd(str):
    """usage:
    if _DEB: logd(f"{str}")
    """
    if _DEB: print(f"[deb] {str}")

### MAIN ###
if __name__ == "__main__":
    if _DEB:
        sys.stdin = io.StringIO(_INPUT)
        print("!! Debug Mode !!")

    ans = main()

    if _DEB:
        print()
        if _EXPECTED.strip() == ans.strip(): print("!! Success !!")
        else: print(f"!! Failed... !!\nANSWER:   {ans}\nExpected: {_EXPECTED}")