x = input()

while x !='0':
    x_list = list(x)
    #print(x_list)
    #print("{0}".format(len(x_list)))
    sum = 0
    for i in range(len(x_list)):
        sum += int(x_list[i])
    print(sum)    
    x = input()