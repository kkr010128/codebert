A = [input().split() for _ in range(3)]
N = int(input())
c = [[False]*3 for _ in range(3)]
for _ in range(N):
    B = input()
    for i in range(3):
        if B in A[i]:
            c[i][A[i].index(B)] = True

def solve(c):
    y = "Yes"
    n = "No"
    for i in range(3):
        if c[i][0] and c[i][1] and c[i][2]:
            return y
        if c[0][i] and c[1][i] and c[2][i]:
            return y
    if c[0][0] and c[1][1] and c[2][2]:
        return y
    if c[0][2] and c[1][1] and c[2][0]:
        return y

    return n

print(solve(c))
