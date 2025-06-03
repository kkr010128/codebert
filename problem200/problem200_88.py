def solve():
    A,B, M = map(int, input().split())
    a_kind = list(map(int, input().split()))
    b_kind = list(map(int, input().split()))
    Coupon =  [list(map(int, input().split())) for _ in range(M)]
    ans = min(a_kind) + min(b_kind)

    for x,y,disc in Coupon:
        ans = min(ans, a_kind[x-1] + b_kind[y-1] - disc)
    print(ans)



if __name__ == '__main__':
    solve()
