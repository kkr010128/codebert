W = "W"
R = "R"

N = int(input())
C = list(input())
numR = C.count(R)
result = 0
for i in range(numR):
    if C[i] == W:
        result += 1
print(result)
