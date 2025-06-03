# -*- coding: utf-8 -*-

def resolve(T,v):
    lv = v
    while lv != T[lv]:
        lv = T[lv]
    T[v] = lv
    return lv

def solve():
    N, M = map(int, input().split())
    T = list(range(N+1))
    for i in range(M):
        u, v = map(int, input().split())
        lu = resolve(T,u)
        lv = resolve(T,v)
        if lv == lu:
            continue
        T[lv] = lu
        #print(f'===round{i}===')
        #print(T)
        #print([resolve(T,v) for v in range(N+1)])
    return len(set(resolve(T,v) for v in range(1,N+1)))-1

if __name__ == '__main__':
    print(solve())

