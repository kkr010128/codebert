import math

numbers = []
n = raw_input()
for i in range(int(n)):
    input_num = raw_input()
    numbers.append(int(input_num))

count = 0
for num in numbers:
    prime_frag = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime_frag = False
            break
    if prime_frag:
        count += 1
print count