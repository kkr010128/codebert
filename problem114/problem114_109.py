D = int(input())
C = [int(x) for x in input().split()]
S = [[int(i) for i in input().split()] for D in range(D)]
T = [0]*D
for i in range(D):
    T[i] = int(input())

score = [0]*26
last = [-1]*26

for i in range(D):
    score[T[i]-1] += S[i][T[i]-1]
    last[T[i]-1] = i

    for j in range(26):
        score[j] -= C[j]*(i-last[j])
    print(sum(score))
