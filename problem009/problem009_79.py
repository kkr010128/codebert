import collections

def breadth_first_search(g,check,length):
    q = collections.deque()
    q.append(1)
    check[1] = 1
    length[1] = 0
    while len(q) != 0:
        v = q.popleft()
        for u in g[v]:
            if check[u] == 0:
                check[u] = 1
                length[u] = length[v]+1
                q.append(u)

    return length

def main():
    N = int(input())
    g = []
    g.append([])
    for i in range(N):
        tmp = input().split()
        tmp_ls = []
        for i in range(int(tmp[1])):
            tmp_ls.append(int(tmp[i+2]))
        g.append(tmp_ls)

    check = [0]*(N+1)
    length = [0]*(N+1)
    ans = breadth_first_search(g,check,length)
    for i in range(N):
        node_num = i+1
        if ans[node_num] == 0 and i != 0:
            ans[node_num] = -1
        print(node_num,ans[node_num])

main()

