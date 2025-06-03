N = int(input())
A = list(map(int, input().split())) # <- note that this has (N - 1) elements
#print(A)
A_0 = [x - 1 for x in A]
#print(A_0)
ans = [0] * N # <- represents number of immediate subordinates of each person

for i in range(0, N - 1):
    ans[A_0[i]] += 1

for i in range(0, N):
    print(ans[i])
