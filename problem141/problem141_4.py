def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n+1):
        s.append(s[-1]+a[~i])
    s.reverse()
    max_nodes = 1
    ans = 0
    for i in range(n+1):
        if a[i] > max_nodes:
            print(-1)
            return
        ans += min(max_nodes, s[i])
        max_nodes -= a[i]
        max_nodes *= 2

    print(ans)
        
    
    
if __name__ == '__main__':
    main()