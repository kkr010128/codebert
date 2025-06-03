# 入力
N = int(input())
A = list(map(int, input().split()))

# 上限を決める
NowNode = 2**0
NextNode = (NowNode - A[0])*2
UpperLimit = [0] * (N+1)
UpperLimit[0] = 1
if A[0] == 1:
    if N == 0:
        print(1)
        exit()
    print(-1)
    exit()
for d in range(1, N+1, 1):
    NowNode = NextNode
    NextNode = (NowNode - A[d]) * 2
    UpperLimit[d] = NowNode
# print(UpperLimit)
UpperLimit[-1] = min(A[-1], UpperLimit[-1])
# 下から見ていく
NowNode = A[-1]
ans = 0

for d in range(N, -1, -1):
    PrevNode = NowNode
    if UpperLimit[d] < A[d]:
        print(-1)
        exit()
    if NowNode + A[d] <= UpperLimit[d]:
        NowNode += A[d]
    else:
        NowNode = UpperLimit[d]
    ans += NowNode
    # print(d, NowNode)
print(ans)
