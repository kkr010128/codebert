line = input()
 
length = len(line)
sum = 0
for i in range(length):
    sum += int(line[i])
 
if sum % 9 == 0:
    print("Yes")
else:
    print("No")