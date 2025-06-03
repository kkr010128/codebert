a, b, c = input().split()

count_devisors = 0
for number in range(int(a), int(b)+1):
    if int(c) % number == 0:
        count_devisors += 1
print(count_devisors)