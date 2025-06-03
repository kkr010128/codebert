# coding: utf-8
import sys
from collections import deque

output_str = deque()
data_cnt =  int(input())  

for i in range(data_cnt):
    in_command = input().rstrip().split(" ")
    
    if in_command[0] == "insert":
        output_str.appendleft(in_command[1])
    elif in_command[0] == "delete":
        if output_str.count(in_command[1]) > 0:
            output_str.remove(in_command[1])
    elif in_command[0] == "deleteFirst":
        output_str.popleft()
    elif in_command[0] == "deleteLast": 
        output_str.pop()

print(" ".join(output_str))