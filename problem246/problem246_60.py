import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    P=LI()
    Q=LI()
    
    
    import itertools
    
    cnt=0
    p=0
    q=0
    for ite in itertools.permutations(range(1,N+1)):
        if P==list(ite):
            p=cnt
        if Q==list(ite):
            q=cnt    
        cnt+=1
        
    print(abs(p-q))
        
        
main()
