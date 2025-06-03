# coding: utf-8
# Your code here!
import numpy as np
import copy

D = int(input())
C = list(map(int,input().split()))
contest = [list(map(int,input().split())) for i in range(D)]
inputs = [int(input()) for i in range(D)]
# print(contest)
# print(inputs)

lists = np.array([0 for i in range(26)])
Y = 0
for i,j in zip(contest,inputs):
    lists += 1
    lists[j-1] = 0
    X = C * lists.T
    # print(X)
    # print(sum(X))
    # x = sum(C[:j-1])+sum(C[j:])
    # y = i[j-1]-x+solve
    Y = i[j-1]-sum(X)+Y
    print(Y)
    Y = copy.deepcopy(Y)