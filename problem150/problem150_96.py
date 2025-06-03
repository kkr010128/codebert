# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**6)
N,K=map(int, sys.stdin.readline().split())
A=[None]+map(int, sys.stdin.readline().split())
visit=[ 0 for _ in range(N+1) ]

L=[]    #閉路になった町番号を順番に記録する

def func(fro):
    global K
    to=A[fro]
    visit[fro]+=1
    if visit[fro]==2:
        L.append(fro)
    if visit[to]<=1:    #閉路ループは2回まで許可する
        K-=1        #操作回数を減らす
        if K==0:    #Kが途中でゼロになれば、その時に移動しようとしていたtoが答え
            print to
            quit()
        func(to)

func(1)
K-=1
l=len(L)
print L[K%l]
