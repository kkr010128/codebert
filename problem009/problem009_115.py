#from collections import deque
import sys

readline = sys.stdin.readline
sys.setrecursionlimit(10**6)

#def mypopleft(que, index):
#    if len(que) > index:
#        return que.pop(index)
#    else:
#        return []


def main():
    # input
    n = int(input())

    graph = []
    for i in range(n):
        u, k, *tmp = [int(i) for i in readline().split()]
        graph.append(tmp)
    
    #print(graph)
    d = [-1]*n
    #que = deque([1])
    que = [1]
    #count = 0
    d[0] = 0
    check = []

    while True:
        v = que.pop(0)
        #print(v)
        #count += 1
        #print(d)
        for u in graph[v-1]:
            #print(u)
            if d[u-1] == -1:
                d[u-1] = d[v-1] + 1
                que.append(u)
        if len(que) == 0:
            break
    
    for i in range(n):
        print("{} {}".format(i+1, d[i]))


if __name__ == "__main__":
    main()

