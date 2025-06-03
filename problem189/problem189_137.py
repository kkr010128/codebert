#

import sys
input=sys.stdin.readline

def main():
    N,M=map(int,input().split())
    if N>=2 and M>=2:
        print((N*(N-1))//2+(M*(M-1)//2))
    elif N>=2:
        print((N*(N-1))//2)
    elif M>=2:
        print((M*(M-1)//2))
    else:
        print(0)
            
    
if __name__=="__main__":
    main()
