n = int(input())
testimonies = [[] for i in range(n)]
for idx1 in range(n):
    count = int(input())
    for idx2 in range(count):
        x,y = map(int, input().split())
        testimonies[idx1].append((x-1, y))

output = 0
for combination in range(2 ** n):
    consistent = True
    for index in range(n):
        if (combination >> index) & 1 == 0:
            continue
        for x,y in testimonies[index]:
            if (combination >> x) & 1 != y:
                consistent = False
                break
        if not consistent:
            break
    if consistent:
        output = max(output, bin(combination)[2:].count("1"))
print(output)