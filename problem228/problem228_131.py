H = int(input())

count = 0
for i in range(10**12):
    if H == 0:
        break
    H = int(H/2)
    count += 2 ** i
    

print(count)