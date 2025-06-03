l = [int(i) for i in input().split()]

a = l[0]
b = l[1]
c = l[2]

yaku = 0

for i in range(b-a+1):
    if c % (i+a) == 0:
        yaku = yaku + 1

print(yaku)