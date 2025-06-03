#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n,a,b = map(int,input().split())
    ans=0
    if (b-a) % 2 == 0:
        print((b-a) // 2)
    else:
        print((b-a)//2 + min(a-1,n-b) + 1)

if __name__=="__main__":
    main()