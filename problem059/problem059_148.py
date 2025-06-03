r, c = map(int, raw_input().split())
matrix = []
sum_line = [0] * c
for i in range(r):
    line = map(int, raw_input().split())
    sum = 0
    for j in range(c):
        sum += line[j]
        sum_line[j] += line[j]
    line.append(sum)
    matrix.append(line)
    #print " ".join(map(str, line))

sum = 0
for i in range(r):
    print " ".join(map(str, matrix[i]))
    sum += matrix[i][c]
sum_line.append(sum)
print " ".join(map(str, sum_line))