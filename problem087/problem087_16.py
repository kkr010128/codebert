def digitsum(n):
    res = 0
    for i in n:
        #print(ni)
        ni = int(i)
        res += ni
    return res 

s = input()
r = digitsum(s)

if r % 9 == 0:
    print("Yes")
else:
    print("No")
