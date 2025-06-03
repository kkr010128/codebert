bank = 100
x = int(input())

i = 1
while 1:
    bank += bank // 100
    if bank >= x:
        break
    i += 1
print(i)