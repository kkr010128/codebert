N = int(input())

result = [0] * (N + 1)

for i in list(map(int, input().split())):
    result[i] += 1

result.pop(0)

for r in result:
    print(r)
