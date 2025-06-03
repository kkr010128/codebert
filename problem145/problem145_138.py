#import time
from itertools import dropwhile, takewhile
def main():
    N, M = list(map(int, input().split()))
    lis = [list(map(int, input().split())) for _ in range(M)]
    #print(lis)
    edge = [[] for _ in range(N+1)]
    #print(edge)
    for a,b in lis:
        edge[a].append(b)
        edge[b].append(a)
        #print(edge)
    ans = [0] * (N+1)
    visited = {0}
    stack = [1]
    for i in stack:
        for j in edge[i]:
            if j in visited:
                continue
            stack.append(j)
            #print(stack)
            visited.add(j)
            #print(visited)
            ans[j]=i
    print("Yes")
    for k in ans[2:]:
        print(k)


if __name__ == '__main__':
    #start = time.time()
    main()
    #elapsed_time = time.time() - start
    #print("経過時間:{}".format(elapsed_time * 1000) + "[msec]")