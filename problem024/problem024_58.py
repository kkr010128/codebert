
def check(P,k,staffList):
    i = 0
    for _ in range(k):
        staffNum = 0
        while(staffNum + staffList[i]<= P):
            staffNum += staffList[i]
            i += 1
            if i == n:
                return n
    return i


def getMaxP(n,k,staffList):
    # Pが増えれば，入れられる個数は単純増加するので，二部探索によりPの最小値を求められる
    left = 0
    right = 100000*10000
    while right-left>1:
        mid = (left+right)//2
        staffNum = check(mid,k,staffList)
        if staffNum >= n :
            right = mid
        else:
            left = mid

    return right


if __name__ == "__main__":
    n,k = map(int,input().split())
    staffList = [int(input()) for _ in range(n)]

    # 特定の最大積載量でどれだけ積めるのかを計算する
    P = getMaxP(n,k,staffList)

    print(P)
