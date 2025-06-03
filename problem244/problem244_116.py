processedIp = input().split(" ")
k = int(processedIp[0])
x = int(processedIp[1])
totalValue = k*500
if (totalValue >= x):
    print("Yes")
else:
    print("No")