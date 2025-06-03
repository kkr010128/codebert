S = input()
sum = 0
for i in range(3):
    if S[i]=="R":
        sum += 1
if sum == 2 and S[1] == "S":
        sum = 1
print(sum)
