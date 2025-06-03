num = int(input())
inVal = input().split()
sum = 0
result = []
for n in range(num):
    result.append(int(inVal[n]))
    sum = sum + int(inVal[n])
print(str(min(result)) + " " + str(max(result)) + " " + str(sum))
