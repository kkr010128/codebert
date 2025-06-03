# encoding: utf-8
from collections import deque

def round_robin_scheduling(N, Q, A):
    t = 0
    while A:
        process = A.popleft()
        if process[1] <= Q:
            t += process[1]
            print(process[0],t) 
        else:
            t += Q
            A.append([process[0],process[1]-Q])

if __name__ == '__main__':
    N,Q = map(int,input().split())
    A = deque()
    for i in range(N):
        a = input()
        A.append([a.split()[0],int(a.split()[1])])

    round_robin_scheduling(N,Q,A) 