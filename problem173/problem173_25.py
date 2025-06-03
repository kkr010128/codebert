n = (int)(input())
ret = 0
for i in range(n+1):
    if i % 3 != 0 and i % 5 != 0:
        ret += i 

print("{}".format(ret))