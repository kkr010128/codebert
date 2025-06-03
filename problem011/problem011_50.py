b, a = map(int, raw_input().split(" "))
if a >= b:
    temp = b
    b = a
    a = temp

while 1:
    r = b % a
    if r == 0:
        print(a)
        break
    b = a
    a = r