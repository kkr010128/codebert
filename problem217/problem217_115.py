N = int(input())
A = list(map(int, input().split()))


i = 0

for i in range(len(A)):
    if (A[i] % 2 == 0):
        if A[i] % 3 != 0 and A[i] % 5 != 0:
            print('DENIED')
            exit()
        else:
            continue
    else:
        continue

print('APPROVED')