number = list(input())
sum = 0
for i in number:
    sum += int(i)
if (sum % 9) == 0 :
    print("Yes")
else:
    print("No")