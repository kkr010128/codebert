import math
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()

def main():
    X = ii()
    print(360//math.gcd(X,360))

if __name__ == "__main__":
  main()
