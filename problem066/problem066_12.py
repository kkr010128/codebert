results = []

while True:
    str_in = input()
    if str_in == '-':
        break
    trial = int(input())

    for i in range(trial):
        h = int(input())
        str_in = str_in[h:] + str_in[:h]

    results.append(str_in)

for result in results:
    print(result)