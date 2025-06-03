import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    A.sort()
    flag=1
    for i in range(N-1):
        if A[i]==A[i+1]:
            flag=0
            break
        
    if flag:
        print("YES")
    else:
        print("NO")

main()
