a = input().split()
sum = 0
for n in a:
    sum += int(n)
print('bust') if sum >= 22 else print('win')