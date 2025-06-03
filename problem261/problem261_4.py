import math

s = input()
ret = 0

s_len = len(s)
count = (int)(math.floor(s_len/2))
for i in range(count):
    if s[i] !=  s[s_len-i-1]:
        ret += 1

print("{}".format(ret))