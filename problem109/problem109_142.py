N = int(input())
results = [input() for _ in range(N)]

C = [0] * 4
dic = ['AC', 'WA', 'TLE', 'RE']

for result in results:
    for i in range(4):
        if result == dic[i]:
            C[i] += 1
            break

for j in range(4):
    print(dic[j] + ' x ' + str(C[j]))