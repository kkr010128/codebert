i = input()
i_l = i.split()
count = 0
for each in range(int(i_l[0]),int(i_l[1])+1):
    if int(i_l[2]) % each == 0:
        count += 1
else:
    print(count)