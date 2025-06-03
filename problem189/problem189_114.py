tmp = input().split(" ")
N = int(tmp[0])
M = int(tmp[1])
 
ans = N * (N - 1) / 2 + M * (M - 1) / 2

print(int(ans))