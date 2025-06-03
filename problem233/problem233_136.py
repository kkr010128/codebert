
def solve():
#    tmp_max = P[0]
    tmp_min = P[0]
    cnt = 1
    for i in range(0,N):
        if P[i] < tmp_min:
            tmp_min = P[i]
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    N = int(input())
    P = list(map(int, input().split()))
    solve()  
