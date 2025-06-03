import warnings


data = 1

i = 0

while (i == 0):
    temp = raw_input().split()

    if (temp[1] == '+'):
        data = int(temp[0]) + int(temp[2])
        print data
    elif (temp[1] == '-'):
        data = int(temp[0]) - int(temp[2])
        print data
    elif (temp[1] == '*'):
        data = int(temp[0]) * int(temp[2])
        print data
    elif (temp[1] == '/'):
        data = int(temp[0]) / int(temp[2])
        print data
    else:
        break