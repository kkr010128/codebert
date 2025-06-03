input_line = list(map(int,input().split(' ')))

if(input_line[0]>=input_line[2]):
    input_line[0] -= input_line[2]
elif((input_line[0]+input_line[1])>=input_line[2]):
    input_line[1] -= (input_line[2]-input_line[0])
    input_line[0] = 0
else:
    input_line[0] = 0
    input_line[1] = 0

print(input_line[0],input_line[1])
