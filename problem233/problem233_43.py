N = int(input())

minP = N
count = 0

for pi in map(int, input().split()):
    minP = min(minP, pi)

    if pi <= minP:
        count += 1

print(count)