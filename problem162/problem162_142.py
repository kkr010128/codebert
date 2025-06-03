import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def main():
    n,m = map(int,input().split())
    x = m//2
    y = m - x
    for i in range(x):
        print(i+1,2*x+1-i)
    for i in range(y):
        print(2*x+2+i,2*x+2*y+1-i)
    
if __name__ == "__main__":
    main()