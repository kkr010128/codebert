#!/usr/bin/env python3
from itertools import product

def solve(n,a):
    testimony = product([0,1],repeat=n)
    ans = 0
    for l in testimony:
        flag = True
        for test in a:
            if l[test[0]] and l[test[1]] and (test[2] == 0):
                flag = False
            if l[test[0]] and l[test[1]]==0 and test[2]:
                flag = False
        if flag:
            ans = max(ans,sum(l))
    return ans



def main():
    N = int(input())
    a = []
    for i in range(N):
        tmp = int(input())
        for _ in range(tmp):
            x,y = map(int,input().split())
            a.append([i,x-1,y])
    print(solve(N,a))
    return

if __name__ == '__main__':
    main()
