n = int(input())
S = [int(i) for i in input().split(' ')]

q = int(input())
T = [int(i) for i in input().split(' ')]

result = 0
for t in T:
    for s in S:
        if t == s:
            result += 1
            break

print(result)
