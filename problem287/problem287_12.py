num = int(input())

data = list()

for i in range(1,10):
    for j in range(1, 10):
        data.append(i*j)

if num in data:
    print('Yes')
else:
    print('No')