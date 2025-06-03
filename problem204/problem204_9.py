S = input()
N = int(input())
line = [''] * (N+1) * 2
rev = False
pos = N
line[pos] = S
leftPos = pos - 1
rightPos = pos + 1

for i in range(N):
    A = input().split()
    if len(A) == 1:
        rev = not rev
    else:
        if A[1] == '1':
            if rev == False:
                pos = leftPos
                leftPos -= 1
            else:
                pos = rightPos
                rightPos += 1
        else:
            if rev == False:
                pos = rightPos
                rightPos += 1
            else:
                pos = leftPos
                leftPos -= 1
        line[pos] = A[2]

ans = line[leftPos+1:rightPos]
ans = "".join(ans)
if rev == False:
    print(ans)
else:
    print(ans[::-1])
