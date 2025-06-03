import sys
sys.setrecursionlimit(10**9)

def main():
    X,Y,A,B,C = map(int,input().split())
    P = sorted(list(map(int,input().split())),reverse=True)
    Q = sorted(list(map(int,input().split())),reverse=True)
    R = list(map(int,input().split()))

    print(sum(sorted(P[:X]+Q[:Y]+R,reverse=True)[:X+Y]))

if __name__ == "__main__":
  main()
