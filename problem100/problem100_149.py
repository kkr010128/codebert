import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    x=I()
    t=1800
    for i in range(10):
        if x>=t:
            print(i+1)
            exit()
        t-=200

main()
