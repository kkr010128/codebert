red, green, blue = map(int, input().split())
k = int(input())
success = 0
for cnt in range(k+1):
    if red >= green:
        green *= 2
    elif red >= blue:
        blue *= 2
    elif green >= blue:
        blue *= 2
    else:
        success = 1
        break
if success == 1:
    print('Yes')
else:
    print('No')