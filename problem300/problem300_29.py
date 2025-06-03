
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
import math
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True  
a,b = map(int,input().split())
a_list = make_divisors(a)
b_list = make_divisors(b)
a_b_and = set(a_list) & set(b_list)
a_b_and = list(a_b_and)


count = 1
for a_b in a_b_and:
  if is_prime(a_b) == True:
    count += 1
    
print(count)