def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N,M = map(int,input().split())
    to = [[] for _ in range(N)]
    for _ in range(M):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        to[a].append(b)        
        to[b].append(a)        
    # print(to)
    guide = [0] * N
    guide[0] = 1
    q = deque()
    q.append(0)
    while len(q) > 0:
        u = q.popleft()
        for v in to[u]:
            # print(guide)
            if guide[v] != 0:
                continue
            guide[v] = u+1
            q.append(v)

    print("Yes")
    for g in guide[1:]:
        print(g)

if __name__ == '__main__':
    main()
