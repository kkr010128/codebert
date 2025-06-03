N = int(input())

count = 0

count += int(N/2)

if int(N/2)-N/2 == 0:
    for i in range(1,int(N/2)):
        if int(N/i)-N/i == 0:
            count += int(N/i)-1
        else:
            count += int(N/i)
else:
    for i in range(1,int(N/2)+1):
        if int(N/i)-N/i == 0:
            count += int(N/i)-1
        else:
            count += int(N/i)

print(count)