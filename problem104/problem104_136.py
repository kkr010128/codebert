digitsArr = list(map(int, input().split()))
multipleConter = 0
for i in range(digitsArr[0], digitsArr[1]+1):
    if i % digitsArr[-1] == 0:
        multipleConter += 1

print(multipleConter)