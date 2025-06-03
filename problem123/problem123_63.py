N = int(input())
A = list(map(int,input().split()))
xor = 0
for i in range(N):
    xor ^= A[i]
anslis = []
for i in range(N):
    answer = xor^A[i]
    anslis.append(answer)
print(' '.join(map(str,anslis)))