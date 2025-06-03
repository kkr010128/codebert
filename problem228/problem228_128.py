n = int(input())
ret = 0
b = 1
while n > 0:
    ret += b
    n //= 2
    b *= 2
print(ret)
    
