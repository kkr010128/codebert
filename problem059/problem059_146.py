r, c = map(int, raw_input().split())

data = [0 for i in range(r)]
temp = [0 for i in range(c)]

for i in range(r):
    data[i] = map(int, raw_input().split())
    
for i in range(r):
    data[i].append(0)
    data[i][c] = sum(data[i])
for i in range(c):
    for j in range(r):
        temp[i] += data[j][i]
temp.append(sum(temp))
data.append(temp)

for i in range(r+1):
    print " ".join(map(str, data[i]))