import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    n,m=MI()
    if n%2:
        for i in range(m):
            print(1+i,n-i)
    else:
        i=1
        j=n//2
        while m and i<j:
            print(i,j)
            i+=1
            j-=1
            m-=1

        i=n//2+2
        j=n
        while m and i<j:
            print(i,j)
            i+=1
            j-=1
            m-=1

main()