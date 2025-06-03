import math

def triangle(co1, co2):
    ans = []
    x1 = co1[0]
    y1 = co1[1]
    x2 = co2[0]
    y2 = co2[1]
    part1 = [(2 * x1 + x2) /3, (2 * y1 + y2) / 3]
    part2 = [(x1 + 2 * x2) /3, (y1 + 2 * y2) / 3]
    #part2をpart1中心に60度回転
    edge = [(part2[0] - part1[0])/2 - (part2[1] - part1[1])/ 2 * math.sqrt(3) + part1[0], (part2[0] - part1[0])/2 * math.sqrt(3) + (part2[1] - part1[1])/ 2 + part1[1]]
    ans.extend([part1, edge, part2, co2])
    return ans
def rec(A, n):
    if n == 0:
        return
    
    rec(A, n-1)
    for i in range(4 ** (n-1)):
        A[n].extend(triangle(A[n-1][i], A[n-1][i+1]))

n = int(input())
koch = [[[0.0, 0.0]] for i in range(n + 1)]
koch[0].append([100.0, 0.0])
rec(koch, n)
for i in range(4 ** n + 1):
    print(*koch[n][i])
