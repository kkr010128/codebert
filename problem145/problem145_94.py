def main():
    n, m = (int(i) for i in input().split())
    graph = { i: [] for i in range(1, n+1) }

    for i in range(m):
        src, dst = (int(i) for i in input().split())
        graph[src].append(dst)
        graph[dst].append(src)

    def bfs():
        st = [1] 
        pptr = { 1: 0 }

        while st:
            room = st.pop(0)
            for dest_room in graph[room]:
                if dest_room in pptr:
                    continue
                st.append(dest_room)
                pptr[dest_room] = room

        return pptr

    pptr = bfs()
    if len(pptr) != n:
        print('No')

    else:
        print('Yes')
        for i in sorted(pptr.keys()):
            if i == 1:
                continue
            print(pptr[i])

main()
