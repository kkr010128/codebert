import math

def is_prime(x):
    if x == 2:
        return True

    if (x == 1) or (x % 2 == 0):
        return False

    for i in range(3, math.ceil(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False

    return True
    
if __name__ == '__main__':
    element_number = int(input())
    input_array = [int(input()) for i in range(element_number)]

    output = 0
    for x in input_array:
        if(is_prime(x)):
            output += 1

    print(output)