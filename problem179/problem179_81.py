import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M=mi()
    A=list(mi())

    sum_vote = sum(A)
    count = 0
    for a in A:
        if a >= sum_vote / (4*M):
            count +=1 
    
    print("Yes" if count >= M else "No")



if __name__ == "__main__":
    main()