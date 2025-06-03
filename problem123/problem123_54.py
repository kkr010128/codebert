N = int(input())
A = list(map(int, input().split()))

b = 0
for a in A:
    b ^= a
for a in A:
    print(b^a, end=" ")
print("")
