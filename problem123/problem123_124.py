#ABC 171 E - Red Scarf

n = int(input())
A = list(map(int, input().split()))

S = 0
for i in A:
    S ^= i

B = [S^i for i in A]
print(*B)
