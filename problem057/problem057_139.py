one = [int(i) for i in input().split()]
data = []
while one != [-1, -1, -1]:
    data.append(one)
    one = [int(i) for i in input().split()]

answer = ['F' if i[0] == -1 or i[1] == -1 else 'A' if i[0] + i[1] >= 80 else 'B' if 65 <= i[0] + i[1] < 80 else 'C' if 50 <= i[0] + i[1] < 65 else 'C' if 30 <= i[0] + i[1] < 50 and 50 <= i[2] else 'D' if 30 <= i[0] + i[1] < 50 else 'F' for i in data]
print(*answer, sep="\n")

