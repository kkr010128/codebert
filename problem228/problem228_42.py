import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    H=I()
    ans=0
    
    def f(x):
        if x==0:
            return 0
        return f(x//2)*2 +1
    
    print(f(H))
        

main()
