# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:04:22 2018
ALDS1_3b_r リングバッファによる実装
@author: maezawa
"""

def fifo_enque(data):
    global tail
    global fifo
    fifo[tail] = data
    tail = (tail+1)%fifo_size
    
def fifo_deque():
    global head
    global fifo
    data = fifo[head]
    head = (head+1)%fifo_size
    return data

fifo_size = 100000
fifo = [0 for _ in range(fifo_size)]
head = 0
tail = 0

n, q = list(map(int, input().split()))
for i in range(n):
    s = input().split()
    data = [s[0], int(s[1])]
    fifo_enque(data)
    
current_time = 0
finished = []
fin_time = []

while True:
    data = fifo_deque()
    if data[1] > q:
        current_time += q
        data[1] -= q
        fifo_enque(data)
    else:
        current_time += data[1]
        finished.append(data[0])
        fin_time.append(current_time)
    if head == tail:
        break

for i in range(n):
    print("{} {}".format(finished[i], fin_time[i]))
        


