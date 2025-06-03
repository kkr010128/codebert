#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import heapq

def main():
    A=[]
    B=[]
    M=[]
    values=[]
    a,b,m = map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    M=[list(map(int,input().split())) for _ in range(m)]

# #割引した組み合わせ
    for m in M:
        values.append(A[m[0]-1]+B[m[1]-1]-m[2])

    heapq.heapify(A)
    heapq.heapify(B)

#最も安い組み合わせ
    cheap=heapq.heappop(A)+heapq.heappop(B)

    print(min(cheap,min(values)))

if __name__=="__main__":
    main()