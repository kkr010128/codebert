a, b = input().split(" ")
x = int(a)
y = int(b)

amt = 0
if x == 1:
    amt += 300000
elif x == 2:
    amt += 200000
elif x == 3:
    amt += 100000

if y == 1:
    amt += 300000
elif y == 2:
    amt += 200000
elif y == 3:
    amt += 100000

if x == 1 and y == 1:
    amt += 400000

print (amt)