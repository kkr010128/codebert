n =int(input())

S = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(n):
    b, f, r, v = map(int, input().split())
    S[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        for k in range(10):
            print(" " + str(S[i][j][k]), end = "")
        print("")
    if i == 3:
        break
    print("####################")