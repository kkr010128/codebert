import sys,math

def is_prime_number(arg):
    arg_sqrt=int(math.floor(math.sqrt(arg)))
    i=2
    while i <=arg_sqrt:
        if arg %i ==0:
            return False
        i+=1

    return True
        
        
n=0
prime_numbers=0
for line in sys.stdin:
    l=int(line)
    if n == 0:
        n=l
        continue

    if is_prime_number(l):
        prime_numbers+=1
        

print prime_numbers