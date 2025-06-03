#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n,k = map(int,input().split())
    n=n%k
    print(min(n,abs(n-k)))

if __name__=="__main__":
    main()