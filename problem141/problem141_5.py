N = int(input())
A = list(map(int, input().split()))

error = False
capacity = [0]
cap = 1
for i, a in enumerate(A):
    cap = cap - a
    if cap < 0:
        error = True
        break
    capacity.append(cap)
    cap *= 2

if error:
    print(-1)
else:
    total = 0
    carry = 0
    for d in range(N, -1, -1):
        cap = capacity[d]
        a = A[d]
        check = carry + a
        if check <= cap:
            total += check
            carry += a
        else:
            total += check
            carry = cap

    print(total)
