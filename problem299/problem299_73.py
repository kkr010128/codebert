N = int(input())
A = [int(a) for a in input().split()]

attend = [0] * N
for i in range(N):
    attend[A[i]-1] = str(i+1)

res = ' '.join(attend)

print(res)