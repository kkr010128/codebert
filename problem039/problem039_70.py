import sys
input_data = input()
input_numbers = input_data.split()

if __name__ == '__main__':
    a = int(input_numbers[0])
    b = int(input_numbers[1])
    c = int(input_numbers[2])

    if (a < b) and (b < c) :
        print('Yes')
    else :
        print('No')
