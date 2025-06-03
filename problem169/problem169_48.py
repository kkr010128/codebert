#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import collections

def main():
    bosses=[]
    count={}
    n = int(input())
    bosses=list(map(int,input().split()))
    ans=[0]*n
    for i in bosses:
        ans[i-1]+=1

    for a in ans:
        print(a)

if __name__=="__main__":
    main()