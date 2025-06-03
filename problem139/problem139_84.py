def Int():
    return int(input())
def Ints():
    return map(int,input().split())
def IntList():
    return list(Ints())
def IntMat(N):
    return [IntList() for i in range(N)]

import sys
sys.setrecursionlimit(4100000)
rl = sys.stdin.readline

H1,M1,H2,M2,K = Ints()

S = (H2-H1)*60+(M2-M1)

print(S-K)