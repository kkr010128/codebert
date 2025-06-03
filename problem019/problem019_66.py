n, q = map(int, raw_input().split())
A = [[0, 0] for i in range(n)]

for i in range(n):
    temp = raw_input().split()
    A[i][0] = temp[0]
    A[i][1] = int(temp[1])

time = 0
while A != []:
    if A[0][1] - q > 0:
        A[0][1] = A[0][1] - q
        time = time + q
        A.append(A.pop(0))
    else:
        print A[0][0],
        print time + A[0][1]
        time = time + A[0][1]
        A.pop(0)