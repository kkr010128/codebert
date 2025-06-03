H = int(input())
temp = 1
for i in range(40):
    temp *= 2
    if H < temp:
        print(pow(2,i+1)-1)
        break