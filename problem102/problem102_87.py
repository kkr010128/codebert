# coding: utf-8
#import math
#import numpy
#N = int(input())
def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    #K =int(input())
    ANS = []
    
    #ANS.append(a)
    for i in range(K,N):
        if A[i-K] < A[i]:
            print("Yes")
        else:
            print("No")
        
        
        #ANS.append(a)
    #print(ANS)
    

if __name__ == '__main__':
    main()