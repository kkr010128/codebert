import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
                      
while True:
    try:
        n = int(raw_input())
        total = 0
        for k in range(n):
            if is_prime(int(raw_input())):
                total +=1
        print total
    except EOFError:
        break    