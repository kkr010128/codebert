n = int(input())
S = [int(x) for x in input().split()]
q = int(input())
T = [int(x) for x in input().split()]


res = 0

for num in T:
    if num in S:
        res += 1

print(res)