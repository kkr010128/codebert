# 二分探索を利用した
N, M = map(int, input().split())
tmp = input().split()

A = [int(tmp[i]) for i in range(N)]
A.sort()
cum_A = [None]*N
cum_A[N-1] = A[N-1]
for i in range(1,N):
    cum_A[N-1-i] = cum_A[N-i] + A[N-1-i]
cum_A.append(0)


def geq(A, cum_A, X, N):  # ある定数X以上になる握手の方法が何通りあるか,Aは昇順sort済み
    sum = 0
    val = 0
    index = 0
    for i in range(N):
        while True:
            if index != N and A[i] + A[N - 1 - index] >= X:
                index += 1
            else:
                sum += index
                val += A[i] * index + cum_A[N-index]
                break
    return sum, val

# 2<=X<=2*Nで二分探索をする
low = 2
high = 2*A[N-1]
while low <= high:
    X = (low + high)//2
    sum, val = geq(A, cum_A, X, N)
    if sum == M:
        break
    elif sum > M:
        low = X+1
    else:
        high = X-1
if sum < M:
    X -= 1
sum, val = geq(A, cum_A, X, N)
ans = val - X*(sum-M)
print(ans)



