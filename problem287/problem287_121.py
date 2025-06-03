num = int(input())
i = 1

while i <= 9:
    j = 1
    while j <= 9:
        if (i * j) / num == 1:
            print("Yes")
            exit()
        else:
            j += 1
    i += 1


print("No")