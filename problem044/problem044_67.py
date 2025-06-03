a, b, c = [int(temp) for temp in input().split()]
count   = 0

for check in range(a, b + 1) :
    if c % check == 0 :
       count += 1

print(count)