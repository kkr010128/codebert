N = int(input())
A = list(map(int, input().split()))
A.reverse()
min_max = [[] for _ in range(N+1)]

def main():
    min_max[0] = [A[0], A[0]]
    for i in range(1, N+1):
        a = A[i]
        pre_min, pre_max = min_max[i-1]
        min_max[i] = [(1+pre_min)//2 +a, pre_max +a]
    min_max.reverse()
    if min_max[0][0] != 1:
        print(-1)
        return
    A.reverse()
    ans = 1
    pre = 1
    for i in range(1, N+1):
        a = A[i-1]
        pre = min(2*(pre -a), min_max[i][1])
        ans += pre
    print(ans)

main()