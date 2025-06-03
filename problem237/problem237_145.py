def solve(XL, N):
    XL.sort(key=lambda x:x[1])
    count = N
    for i in range(1, N):
        if XL[i][0] < XL[i-1][1]:
            XL[i][1] = XL[i-1][1]
            count -= 1
    return count
N = int(input())
XL = []
for i in range(N):
    x, l = map(int, input().split(' '))
    XL.append([x-l, x+l])
print(solve(XL, N))   