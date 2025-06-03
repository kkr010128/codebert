A = []
B = []
for i in range(3):
    a = list(map(int, input().split()))
    A.append(a)

N = int(input())

test = [[0]*3 for _ in range(3)]

for i in range(N):
    B.append(int(input()))

for b in B:
    for m in range(3):
        for n in range(3):
            if b == A[m][n]:
                test[m][n] =1

ans = 'No'

for i in range(3):
    if sum(test[i]) == 3:
        ans = 'Yes'
    if test[0][i]+test[1][i]+test[2][i] == 3:
        ans = 'Yes'

if test[0][0]+test[1][1]+test[2][2] == 3:
    ans = 'Yes'

if test[2][0]+test[1][1]+test[0][2] == 3:
    ans = 'Yes'

print(ans)
