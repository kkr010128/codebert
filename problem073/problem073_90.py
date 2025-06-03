n = int(input()) - 1

j = 0

ans = 0

for i in range(1, n):
    
    j = i
    
    while True:
        j += 1
        if i * j > n:
            break
        ans += 1

k = 1

er = 0

while True:
    if k ** 2 > n:
        break
    er += 1
    k += 1

print((ans * 2) + er)