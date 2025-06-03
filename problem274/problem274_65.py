import sys
#input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    s = str(input())
    s = list(reversed(s))
    ans = []
    now = 0
    while now < N:
        for i in reversed(range(min(M,N-now))):
            i += 1
            if s[now+i] == "0":
                now += i
                ans.append(i)
                break
            if i == 1:
                print(-1)
                exit()
        
    print(*reversed(ans))
        
if __name__ == "__main__":
    main()
