# coding: utf-8

import itertools

data_set = []
answer = []

while (1):
    n,x = map(int, input().split())
    if (n == 0 and x == 0):
        break
    data_set.append([n,x])

for d in data_set:
    num = list(range(d[0] + 1))[1:]
    counter = 0
    for i in itertools.combinations(num, 3):
        if (sum(i) == d[1]):
            counter += 1
    answer.append(counter)
    
for ans in answer:
    print(ans)