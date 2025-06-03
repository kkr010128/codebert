n = int(input())
title = []
time = []
for i in range(n):
    line = input().split()
    title += [line[0]]
    time += [int(line[1])]
key = input()
a = title.index(key)
print(sum(time[a+1:]))
