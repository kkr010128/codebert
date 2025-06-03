''' ===========================================
from collections import deque
    appendleft() = push_front(), append = push_back()
    popfleft() = pop_front(), pop() = pop_back()
import heapq #heappush(trgt, val) heappop(trgt) trgt[0] __lt__<
=========================================== '''
##======================================python3
import sys
import collections
from sys import stdin #read(), readline()

sys.setrecursionlimit(10**6)
INF = 1<<50
MINI = 100005

class gv:
    input = None;
    
def build():
    gv.str = input()

def solve():
    slen = len(gv.str)
    if (slen&1) == 1:
        print("No")
        return
    
    for i in range(0,slen,2):
        if (gv.str[i:i+2] == "hi") :
            pass
        else :
            print("No")
            return
    
    print("Yes")
    
    

if __name__ == '__main__':
    build()
    solve()

