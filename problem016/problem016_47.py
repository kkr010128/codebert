N = int(input())
B = input().split()
S = B[:]

for i in range(N):
    for j in range(N-1, i, -1):
        if B[j][1] < B[j-1][1]:
            B[j], B[j-1] = B[j-1], B[j]
    
    m = i
    for j in range(i, N):
        if S[m][1] > S[j][1]:
            m = j
    S[m], S[i] = S[i], S[m]

print(*B)
print('Stable')
print(*S)
print(['Not s', 'S'][B==S] + 'table')