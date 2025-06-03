import math

N = int(input())

divisor_N1=set()
for i in range(1, math.floor(math.sqrt(N-1)) + 1):
    if (N - 1) % i == 0:
        divisor_N1.add(i)
        divisor_N1.add((N-1) // i)
#print(divisor_N1)

divisor_N=set()
for i in range(1, math.floor(math.sqrt(N) + 1)):
    if N % i == 0:
        divisor_N.add(i)
        divisor_N.add(N // i)
#print(divisor_N)
divisor_N.remove(1)
divisor_N1.remove(1)
#print(divisor_N)
#print(divisor_N1)

cnt = len(divisor_N1)
for num in divisor_N:
    temp = N
    while temp % num == 0:
        temp //= num
    if temp % num == 1:
        cnt += 1
        #print(num)
print(cnt)