from collections import deque

def main():
    n, m = map(int, input().split())
    to = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        to[a].append(b)
        to[b].append(a)
    q = deque([1])
    ans = [None]*(n+1)
    while q:
        p = q.pop()
        for child in to[p]:
            if ans[child] is None:
                ans[child] = p
                q.appendleft(child)
    print("Yes")
    print("\n".join(list(map(str, ans[2:]))))
    
    

if __name__ == "__main__":
    main()