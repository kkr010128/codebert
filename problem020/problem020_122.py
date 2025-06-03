# coding: utf-8
import sys
from collections import deque

output_str = deque()
data_cnt =  int(input())  

for i in range(data_cnt):
    line = input().rstrip()
    if line.find(" ") > 0:
        in_command, in_str = line.split(" ")
    else:
        in_command = line
    
    if in_command == "insert":
        output_str.appendleft(in_str)
    elif in_command == "delete":
        if output_str.count(in_str) > 0:
            output_str.remove(in_str)
    elif in_command == "deleteFirst":
        output_str.popleft()
    elif in_command == "deleteLast": 
        output_str.pop()

print(" ".join(output_str))