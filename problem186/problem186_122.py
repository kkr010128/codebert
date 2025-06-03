#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    houses=[]
    k,n=map(int,input().split())
    houses=list(map(int,input().split()))
    distance=[]
    
    for i in range(1,n):
        distance.append(houses[i]-houses[i-1])
    distance.append(k-(houses[-1]-houses[0]))

    max_length=max(distance)    
    print(sum(distance)-max_length)

if __name__=="__main__":
    main()