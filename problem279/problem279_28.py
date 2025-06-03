import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    S=list(input())

    if N%2==1:
        print("No")
        exit()
    
    if S[:N//2] == S[N//2:]:
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
    main()