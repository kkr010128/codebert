from functools import reduce
N = int(input())
A = [int(n) for n in input().split()]
X = reduce(int.__xor__, A)
ans = [X^a for a in A]
print(*ans)