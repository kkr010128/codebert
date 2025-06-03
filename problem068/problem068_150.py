#1st line
input_str = input().strip()

#2nd line
command_max_times = int(input().strip())
command_cnt = 0

while command_cnt < command_max_times:
    command_cnt = command_cnt + 1
    input_line = input().strip().split(" ")
    
    input_command = input_line[0]
    input_sta = int(input_line[1])
    input_end = int(input_line[2])
    
    if input_command == "print":
        print(input_str[input_sta:input_end+1])
    elif input_command == "replace":
        str_replace = input_line[3]
        input_str = input_str[:input_sta] + str_replace + input_str[input_end+1:]
    elif input_command == "reverse":
        str_temp = input_str[input_sta:input_end+1]
        input_str = input_str[:input_sta] + str_temp[::-1] + input_str[input_end+1:]