data = {
        'S': [int(x) for x in range(1,14)],
        'H': [int(x) for x in range(1,14)],
        'C': [int(x) for x in range(1,14)],
        'D': [int(x) for x in range(1,14)]
        }

count = int(input())

for c in range(count):
    (s, r) = input().split()
    r = int(r)

    del data[s][data[s].index(r)]


for i in ('S', 'H', 'C', 'D'):
    for v in data[i]:
        print(i, v)