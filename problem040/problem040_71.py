num = list(map(int,input().split()))
count = 0
while count < 2:
        for i in range(2):
                j = 0
                if num[i] > num[i+1]:
                        j = num[i]
                        num[i] = num[i+1]
                        num[i+1] = j
                else:
                        continue
        count += 1
out = ''
for i in num:
        out += str(i) + ' '
print(out[:-1])