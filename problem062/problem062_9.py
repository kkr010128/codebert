data = []
while True:
    x = input().strip()
    if x == '0':
        break
    data.append(list(map(int, list(x))))

for i in range(len(data)):
    print(sum(data[i]))