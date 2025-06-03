N = int(input())
A = []
for i in range(N):
    a = int(input())
    xy = [list(map(int, input().split())) for _ in range(a)]
    A.append([a, xy])
# print(A)

# 下からi桁目のbitが1->人iは正直
# 下からi桁目のbitが0->人iは不親切
# 不親切な人の証言は無視して良い

ans = 0
for i in range(2**N):
    for j in range(N):
        flag = 0
        if (i >> j) & 1:
            for k in range(A[j][0]):
                l = A[j][1][k][0]
                m=A[j][1][k][1]
                # print(i,j,k,(l,m),(i >> (l-1)))
                if not (i >> (l-1)) & 1 == A[j][1][k][1]:
                    flag = 1
                    break
            if flag == 1:
                break
    else:
        # print(bin(i))
        ct = 0
        for l in range(N):
            ct += ((i >> l) & 1)
        ans = max(ans, ct)
print(ans)
