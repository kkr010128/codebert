n = list(map(int, list(input())))
count = 0
n = n[::-1] + [0]

for idx, num in enumerate(n):
    if num == 10:
        n[idx+1] += 1
    elif num == 5:
        if n[idx+1] >= 5:
            n[idx+1] += 1
            count += 10 - num
        else:
            count += num

    elif num <= 4:
        count += num
    else:
        count += 10 - num
        n[idx+1] += 1

print(count)