N = int(input())
A = list(map(int, input().split()))

answer = 'DENIED'
for i in range(0, N):
    if A[i] % 2 == 0:
        if A[i] % 3 == 0 or A[i] % 5 == 0:
            answer = 'APPROVED'
        else:
            answer = 'DENIED'
            break
    else:
        answer = 'APPROVED'

print(answer)