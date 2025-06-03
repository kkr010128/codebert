# coding: utf-8
# Your code here!

num_str = "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"
num_str = num_str.split(", ")
input_str = input()

print(num_str[int(input_str)-1])