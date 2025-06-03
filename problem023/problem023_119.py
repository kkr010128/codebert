command_num = int(input())
dict = set([])

for i in range(command_num):
    in_command, in_str = input().rstrip().split(" ")
    
    if in_command == "insert":
        dict.add(in_str)
    elif in_command == "find":
        if in_str in dict:
            print("yes")
        else:
            print("no")