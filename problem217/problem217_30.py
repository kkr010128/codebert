N = int(input())
data = list(map(int,input().split()))
sw1 = 0
sw2 = 0
for i in range(0,len(data)):
    if data[i] % 2 == 0:
        sw1 += 1
        if data[i] % 3 == 0 or data[i] % 5 == 0:
            sw2 += 1

if sw1 >= 0 and sw1 == sw2:
    print("APPROVED")
else:
    print("DENIED")