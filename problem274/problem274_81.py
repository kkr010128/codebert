import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    S = input()
    
    ans = []
    check = [False] * (N+1)
    
    idx = N
    while 0 < idx:
        f = False
        for i in range(M, 0, -1):
            if idx-i < 0: continue
            if S[idx-i] == '1':
                if check[idx-i]: print(-1); sys.exit()
                else: check[idx-i] = True
            else:
                ans.append(i)
                idx -= i
                f = True
                break
        if not f: print(-1); sys.exit()
    
    for a in ans[::-1]: print(a)
if __name__ == '__main__':
    main()