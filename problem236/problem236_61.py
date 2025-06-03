H = int(input())
W = int(input())
N = int(input())

count1 = 0
count2 = 0
for i in range(1,W+1):
    count1 += 1
    if i*H >= N:
        break
for j in range(1,H+1):
    count2 += 1
    if j*W >= N:
        break
if count1 > count2:
    print(count2)
else:
    print(count1)