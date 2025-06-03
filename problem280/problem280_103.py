import itertools
n = int(input())
test = list(itertools.permutations([i for i in range(n)]))
data = []
for i in range(n):
    x,y = map(int,input().split())
    data.append([x,y])
total = 0
for i in test:
    for k in range(n-1):
        total += ((data[i[k]][0] - data[i[k+1]][0])**2 + (data[i[k]][1] - data[i[k+1]][1])**2 )**0.5
print(total/len(test))