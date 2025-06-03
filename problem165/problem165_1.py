N = int(input())
li = list()
for i in range(N):
    li.append(input())

print(len(list(set(li))))