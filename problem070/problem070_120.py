def main():
    def find(target):
        if parent[target] < 0:
            return target
        else:
            parent[target] = find(parent[target])
            return parent[target]

    def is_same(x, y):
        return find(x) == find(y)

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return
        if parent[root_x] > parent[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_x] += parent[root_y]
        parent[root_y] = root_x

    # 今回これ使わないけど、どこに誰がいるのかはこれでわかる
    def members(n, x):
        root = find(x)
        return [i for i in range(n) if find(i) == root]

    def get_size(x):
        return -parent[find(x)]

    def get_root():
        return [i for i, root in enumerate(parent) if root < 0]
    
    n, m = map(int, input().split())
    parent = [-1 for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        union(a, b)
    ans = len(get_root()) - 1
    print(ans)

if __name__ == '__main__':
    main()