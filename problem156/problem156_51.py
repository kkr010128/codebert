x = int(input())
for i in range(243):
    for j in range(243):
        if (i-121)**5 - (j-121)**5 == x:
            print(i-121,j-121)
            exit()