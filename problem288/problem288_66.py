import math
N = int(input())

start_digit = math.ceil(math.sqrt(N))

for i in range(start_digit, 0, -1):
    q, r = divmod(N, i)
    if r == 0:
        output = i+q-2
        break
        
print(output)