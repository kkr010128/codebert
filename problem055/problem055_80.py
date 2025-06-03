n = int(input())
count = list()
for b in range(4):
    count.append(list())
    for f in range(3):
        count[b].append(list())
        for r in range(10):
            count[b][f].append(0)

read = 0
while read < n:
    b,f,r,v = [int(x) for x in input().split(" ")]
    count[b-1][f-1][r-1] += v
    read += 1

for b in range(len(count)):
    for f in range(len(count[b])):
        for r in range(len(count[b][f])):
            print("", count[b][f][r], end="")
        print()
    if b < len(count) - 1:
        print("####################")