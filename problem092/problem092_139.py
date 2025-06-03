import math

x,k,d = map(int,input().split())

abs_x = abs(x)

max_len = math.ceil(abs_x/d)*d
min_len = max_len-d

if abs_x-k*d >= 0:
    print(abs_x-k*d)
    exit()

if (math.ceil(abs_x/d)-1)%2 == k%2:
    print(abs(abs_x-min_len))
else:
    print(abs(abs_x-max_len))