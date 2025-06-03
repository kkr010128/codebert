input_num = int(input())
input_str = input()
if len(input_str) <= input_num:
    print(input_str)
else:
    print(input_str[:input_num]+"...")