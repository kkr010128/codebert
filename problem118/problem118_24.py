import math

N = int(input())
s = 0

# def devisor(x):
#     count = 0
#     for i in range(1,math.floor(math.sqrt(x))+1):
#         if (x % i) == 0:
#             count += 2
#             if i**2 == x:
#                 count -= 1
#     return count

# for i in range(1, N+1):
#     s += i * devisor(i)

for i in range(1,N+1):
    y = math.floor(N/i)
    s += y*(y+1)*i//2

print(s)