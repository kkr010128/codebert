# C - Go to School TLE
N = int(input())
A = list(map(int, input().split()))

attend = [i for i in range(1,N+1)]
for j in range(1,N+1):
    attend[A[j-1] - 1] = j
print(*attend)