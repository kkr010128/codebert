#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import itertools

def main():
    n = int(input())
    P=tuple(map(int,input().split()))
    Q=tuple(map(int,input().split()))

    permutations = list(itertools.permutations(range(1,n+1)))
    a = permutations.index(P)
    b = permutations.index(Q)
    print(abs(a-b))    

if __name__=="__main__":
    main()