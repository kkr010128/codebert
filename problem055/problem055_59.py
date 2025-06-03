Residents = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())
for l in range(n):
    b, f, r, v = list(map(int, input().split()))
    Residents[b-1][f-1][r-1] += v
for k in range(4):
    for j in range(3):
        print(' '+' '.join(map(str, Residents[k][j])))
    if k == 3:
        break
    print('####################')