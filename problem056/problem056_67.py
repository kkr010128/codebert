#coding:utf-8
#1_6_D 2015.4.5
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for i in range(n)]
vector = [int(input()) for i in range(m)]
for i in range(n):
    print(sum([matrix[i][j] * vector[j] for j in range(m)]))