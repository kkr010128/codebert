A = [0] * 10

B = list(map(int, input().split()))
for i in range(len(B)):
    A[B[i]] += 1

for i in range(len(A)):
    if A[i] == 2:
        print('Yes')
        break
else:
    print('No')
