line1 = input()
line2 = input()

aryLine1 = line1.split()
arystrLine2 = line2.split()

K = int(aryLine1[0]);
N = int(aryLine1[1]);

aryLine2 = [int(s) for s in arystrLine2]
#print(aryLine2)

aryLine2.sort()
#print(aryLine2)

ans = K

for i in range(0, N):
    temp1 = int(aryLine2[i])
    if i == N - 1:
        temp2 = int(aryLine2[0]) + K
    else:
        temp2 = int(aryLine2[i + 1])

    temp = temp1 - temp2 + K

    if temp < ans:
        ans = temp

print(ans)