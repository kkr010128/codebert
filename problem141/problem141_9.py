import math
N = int(input())
A = list(map(int, input().split()))
section = [[A[-1], A[-1]]]
for i in range(1, N+1):
    min_section = math.ceil(section[i-1][0] / 2) + A[-i-1]
    max_section = section[i-1][1] + A[-i-1]
    section.append([min_section, max_section])
section = section[::-1]

if section[0][0] > 1:
    print(-1)
    exit()

node = [1]

for i in range(1, N+1):
    node.append(min((node[i-1] - A[i-1]) * 2, section[i][1]))

print(sum(node))