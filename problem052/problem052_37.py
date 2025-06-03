def nabeatsu(n):
    if(n % 3 == 0):
        return True
    temp = n
    while(temp > 0):
        if(temp % 10 == 3):
            return True
        temp = temp // 10
    return False

x = int(input())
for i in range(x):
    if(nabeatsu(i + 1)):
        print(' ', end = '')
        print(i + 1, end = '')
print()
