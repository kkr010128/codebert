values = []
while True:
    v = int(input())
    if 0 == v:
        break
    values.append(v)

for i, v in enumerate(values):
    print('Case {0}: {1}'.format(i + 1, v)) 