import math
A, B = map(int, input().split())
answer = -1
for x in range(10000):
    if math.floor(x * 0.08) == A and math.floor(x * 0.10) == B:
        answer = x
        break
print(answer)