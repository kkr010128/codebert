import sys
input = sys.stdin.readline

n, s, c = int(input()), [[0 for i in range(10)] for j in range(10)], 0
for i in range(1, n+1): s[int(str(i)[0])][int(str(i)[-1])] += 1
print(sum([s[i][j] * s[j][i] for i in range(1, 10) for j in range(1, 10)]))