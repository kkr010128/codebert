import sys
input = sys.stdin.readline
def main():
    N  = int(input())
    R = [[] for i in range(N)]
    for i in range(N):
        A = int(input())
        R[i] = [list(map(int, input().split())) for i in range(A)]
    ans = 0
    for i in range(1<<N):
        CNT = 0
        for j in range(N):
            if not (i>>j & 1):
                continue
            CNT += 1
            for x, y in R[j]:
                if y == 1 and (i>>(x-1) & 1):
                    continue
                elif y == 0 and (not (i>>(x-1) & 1)):
                    continue
                else:
                    CNT = 0
                    break
            else:
                continue
            break

        ans = max(ans, CNT)
    print(ans)

if __name__ == '__main__':
    main()