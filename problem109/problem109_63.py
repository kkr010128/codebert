N = int(input())
S = list()
for i in range(N):
    S.append(input())

judge = ['AC', 'WA', 'TLE', 'RE']
count = [0] * 4

for i in range(N):
    letter = S[i]
    ind = judge.index(letter)
    count[ind] += 1

for i in range(len(judge)):
    print(judge[i], "x", str(count[i]))
