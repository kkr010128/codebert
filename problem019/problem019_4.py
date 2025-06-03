# -*- coding: utf-8 -*-

from collections import deque

queue = deque()
input_list = [int(i) for i in input().split()]
for i in range(input_list[0]):
    proc = input().split()
    queue.append([proc[0],int(proc[1])])

count = 0
while len(queue) != 0:
    proc = queue.popleft()
    if input_list[1] < proc[1]:
        queue.append([proc[0],proc[1]-input_list[1]])
        count += input_list[1]
    else:
        count += proc[1]
        print(proc[0] + ' ' + str(count))