x = input()
count = int(x.split()[0])
num = int(x.split()[1])

if count < 10:
    num = num + (100 * (10 - count))
else:
    num

print(num)